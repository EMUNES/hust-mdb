# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Test(models.Model):
    系列 = models.TextField(blank=True, null=True)
    牌号 = models.TextField(blank=True, null=True)
    制造商 = models.TextField(blank=True, null=True)
    链接 = models.TextField(blank=True, null=True)
    材料名称缩写 = models.TextField(blank=True, null=True)
    材料类型 = models.TextField(blank=True, null=True)
    数据来源 = models.TextField(blank=True, null=True)
    上次修改日期 = models.TextField(blank=True, null=True)
    测试日期 = models.TextField(blank=True, null=True)
    数据状态 = models.TextField(blank=True, null=True)
    材料id = models.IntegerField(db_column='材料ID', blank=True, null=True)  # Field name made lowercase.
    等级代码 = models.TextField(blank=True, null=True)
    供应商代码 = models.TextField(blank=True, null=True)
    纤维_填充物 = models.TextField(db_column='纤维/填充物', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    模具表面温度 = models.FloatField(blank=True, null=True)
    熔体温度 = models.FloatField(blank=True, null=True)
    模具温度范围_最小值_field = models.FloatField(db_column='模具温度范围（最小值）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    模具温度范围_最大值_field = models.FloatField(db_column='模具温度范围（最大值）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    熔体温度范围_最小值_field = models.FloatField(db_column='熔体温度范围（最小值）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    熔体温度范围_最大值_field = models.FloatField(db_column='熔体温度范围（最大值）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    绝对最大溶体温度 = models.FloatField(blank=True, null=True)
    顶出温度 = models.FloatField(blank=True, null=True)
    最大剪切应力 = models.FloatField(blank=True, null=True)
    最大剪切速率 = models.FloatField(blank=True, null=True)
    熔体密度 = models.FloatField(blank=True, null=True)
    固体密度 = models.FloatField(blank=True, null=True)
    pvt_b5 = models.FloatField(db_column='pvt-b5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b6 = models.FloatField(db_column='pvt-b6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b1m = models.FloatField(db_column='pvt-b1m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b2m = models.FloatField(db_column='pvt-b2m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b3m = models.FloatField(db_column='pvt-b3m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b4m = models.FloatField(db_column='pvt-b4m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b1s = models.FloatField(db_column='pvt-b1s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b2s = models.FloatField(db_column='pvt-b2s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b3s = models.FloatField(db_column='pvt-b3s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b4s = models.FloatField(db_column='pvt-b4s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b7 = models.FloatField(db_column='pvt-b7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b8 = models.FloatField(db_column='pvt-b8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b9 = models.FloatField(db_column='pvt-b9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    弹性模量e1 = models.FloatField(db_column='弹性模量E1', blank=True, null=True)  # Field name made lowercase.
    弹性模量e2 = models.FloatField(db_column='弹性模量E2', blank=True, null=True)  # Field name made lowercase.
    泊松比v12 = models.FloatField(blank=True, null=True)
    泊松比v23 = models.FloatField(blank=True, null=True)
    剪切模量g12 = models.FloatField(db_column='剪切模量G12', blank=True, null=True)  # Field name made lowercase.
    热膨胀数据横向各向同性系数alpha1 = models.FloatField(blank=True, null=True)
    热膨胀数据横向各向同性系数alpha2 = models.TextField(blank=True, null=True)
    七参数n = models.FloatField(blank=True, null=True)
    七参数tau_field = models.FloatField(db_column='七参数Tau*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    七参数d1 = models.FloatField(db_column='七参数D1', blank=True, null=True)  # Field name made lowercase.
    七参数d2_field = models.FloatField(db_column='七参数D2·', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    七参数d3 = models.FloatField(db_column='七参数D3', blank=True, null=True)  # Field name made lowercase.
    七参数a1 = models.FloatField(db_column='七参数A1', blank=True, null=True)  # Field name made lowercase.
    七参数a2 = models.FloatField(db_column='七参数A2', blank=True, null=True)  # Field name made lowercase.
    c1 = models.TextField(blank=True, null=True)
    c2 = models.TextField(blank=True, null=True)
    转换温度 = models.TextField(blank=True, null=True)
    mfr温度 = models.TextField(db_column='MFR温度', blank=True, null=True)  # Field name made lowercase.
    mfr载入 = models.TextField(db_column='MFR载入', blank=True, null=True)  # Field name made lowercase.
    测量的mfr = models.TextField(db_column='测量的MFR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'
