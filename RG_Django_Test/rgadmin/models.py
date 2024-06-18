from django.db import models

# Create your models here.


class AuthGroupsUsers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    group = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'auth_groups_users'


class AuthIdentities(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255)
    secret2 = models.CharField(max_length=255, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    force_reset = models.IntegerField()
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'auth_identities'
        unique_together = (('type', 'secret'),)


class AuthLogins(models.Model):
    ip_address = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField()
    success = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'auth_logins'


class AuthPermissionsUsers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    permission = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'auth_permissions_users'


class AuthRememberTokens(models.Model):
    selector = models.CharField(unique=True, max_length=255)
    hashedvalidator = models.CharField(db_column='hashedValidator', max_length=255)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING)
    expires = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'auth_remember_tokens'


class AuthTokenLogins(models.Model):
    ip_address = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField()
    success = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'auth_token_logins'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)
    displayname = models.CharField(max_length=250)
    status = models.CharField(max_length=255, blank=True, null=True)
    status_message = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    last_active = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'users'