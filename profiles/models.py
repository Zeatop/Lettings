from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    """
    Modèle représentant le profil d'un utilisateur.

    Cette classe étend les informations de l'utilisateur Django standard
    en ajoutant des données spécifiques à l'application, comme la ville favorite.
    Chaque profil est associé à un utilisateur unique via une relation OneToOne.

    Attributes:
        user (User): Utilisateur Django associé au profil (relation OneToOne).
        favorite_city (str): Ville favorite de l'utilisateur (optionnel, max 64 caractères).

    Examples:
        >>> from django.contrib.auth.models import User
        >>> user = User.objects.create_user('john', 'john@example.com', 'password')
        >>> profile = Profile.objects.create(user=user, favorite_city='Paris')
        >>> print(profile.get_display_name())
        'john'
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):

        """
        Représentation textuelle du profil.

        Returns:
            str: Nom d'utilisateur associé au profil.
        """

        return self.user.username
