from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):

    """
    Modèle représentant une adresse physique.

    Cette classe stocke les informations d'adresse associées aux locations,
    incluant le numéro, la rue, la ville, l'état, le code postal et le code pays.

    Attributes:
        number (int): Numéro de rue (1-9999).
        street (str): Nom de la rue (max 64 caractères).
        city (str): Nom de la ville (max 64 caractères).
        state (str): Code d'état sur 2 caractères.
        zip_code (int): Code postal (1-99999).
        country_iso_code (str): Code pays ISO sur 3 caractères.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):

        """
        Représentation textuelle de l'adresse.

        Returns:
            str: Format "numéro rue".
        """

        return f'{self.number} {self.street}'


class Letting(models.Model):

    """
    Modèle représentant une location.

    Cette classe associe un titre descriptif à une adresse spécifique,
    représentant une propriété disponible à la location.

    Attributes:
        title (str): Titre de la location (max 256 caractères).
        address (Address): Adresse associée à la location (relation OneToOne).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):

        """
        Représentation textuelle de la location.

        Returns:
            str: Titre de la location.
        """

        return self.title
