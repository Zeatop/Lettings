from django.db import migrations, models
import django
from django.contrib.auth.models import User

def forwards_func(apps, schema_editor):

    db_alias = schema_editor.connection.alias
    
    # Récupérer les anciens modèles
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    
    # Récupérer les donbnées des anciens modèles
    old_profiles = OldProfile.objects.using(db_alias).all()
    
    # Récupérer les nouveaux modèles
    NewProfile = apps.get_model("profiles", "Profile")

    for old_profile in old_profiles:
       NewProfile.objects.using(db_alias).create(
           user=old_profile.user,
            favorite_city=old_profile.favorite_city,
       )

class Migration(migrations.Migration):
    dependencies = [("oc_lettings_site", "0001_initial")]

    operations = [
    # D'abord créer les tables pour les nouveaux modèles
    migrations.CreateModel(
        name='Profile',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('favorite_city', models.CharField(blank=True, max_length=64)),
            ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.User')),
        ],
    ),
    # Ensuite transférer les données
    migrations.RunPython(forwards_func),
]