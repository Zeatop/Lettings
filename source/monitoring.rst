Monitoring et observabilité
============================

Intégration Sentry
-------------------

Le projet utilise **Sentry SDK** pour le monitoring des erreurs et des performances.

**Configuration dans ``settings.py`` :**

.. code-block:: python

   import sentry_sdk
   from sentry_sdk.integrations.django import DjangoIntegration
   
   sentry_sdk.init(
       dsn="https://505a28f623ff3376de2f4092d8515558@o4509147190460416.ingest.de.sentry.io/4509162976182352",
       integrations=[DjangoIntegration()],
       traces_sample_rate=1.0,
       profiles_sample_rate=1.0,
       send_default_pii=True,
       environment="development",
   )

**Fonctionnalités Sentry :**

* Capture automatique des erreurs Django
* Profiling des performances
* Tracking des transactions
* Association des erreurs aux utilisateurs
* Environnements séparés (development/production)

Endpoint de test
----------------

Un endpoint de test est disponible pour vérifier l'intégration Sentry :

.. code-block:: python

   # URL : /sentry-debug/
   def trigger_error(request):
       return 1 / 0