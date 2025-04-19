import django
from django.db import migrations, models

def forwards_func(apps, schema_editor):

    db_alias = schema_editor.connection.alias
    
    # Récupérer les anciens modèles
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    
    # Récupérer les donbnées des anciens modèles
    old_addresses = OldAddress.objects.using(db_alias).all()
    old_lettings = OldLetting.objects.using(db_alias).all()
    
    # Récupérer les nouveaux modèles
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    for old_address in old_addresses:
       new_address = NewAddress.objects.using(db_alias).create(
           number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
       )

       for old_letting in OldLetting.objects.using(db_alias).filter(address_id=old_address.id):
            NewLetting.objects.using(db_alias).create(
                title=old_letting.title,
                address=new_address
            )
    

class Migration(migrations.Migration):
    dependencies = [("oc_lettings_site", "0001_initial")]

    operations = [
    # D'abord créer les tables pour les nouveaux modèles
    migrations.CreateModel(
        name='Address',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
            ('street', models.CharField(max_length=64)),
            ('city', models.CharField(max_length=64)),
            ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
            ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
            ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
        ],
    ),
    migrations.CreateModel(
        name='Letting',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title', models.CharField(max_length=256)),
            ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
        ],
    ),
    # Ensuite transférer les données
    migrations.RunPython(forwards_func),
]
    