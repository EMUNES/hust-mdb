from django.db import models
from django.db.models.fields import CharField, FloatField
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Add token when create users automatically.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Material(models.Model):
    series = CharField(db_column="系列", verbose_name="系列", max_length=100)
    mark = CharField(db_column="牌号", verbose_name="牌号", max_length=100)
    manufacturer = CharField(db_column="制造商", verbose_name="制造商",  max_length=50)
    link = CharField(db_column="链接", verbose_name="链接", max_length=100)
    acronym = CharField(db_column="材料名称缩写", verbose_name="材料名称缩写", max_length=20)
    material_type = CharField(db_column="材料类型", verbose_name="材料类型", max_length=100)
    data_source = CharField(db_column="数据来源", verbose_name="数据来源", max_length=100)
    last_modified_date = CharField(db_column="上次修改日期", verbose_name="上次修改日期", max_length=50)
    test_date = CharField(db_column="测试日期", verbose_name="测试日期", max_length=50)
    data_status = CharField(db_column="数据状态", verbose_name="数据状态", max_length=50)
    material_id = CharField(db_column="材料ID", verbose_name="材料ID", max_length=20)
    level_code = CharField(db_column="等级代码", verbose_name="等级代码", max_length=50)
    vendor_code = CharField(db_column="供应商代码", verbose_name="供应商代码", max_length=50)
    fibre_or_infill = CharField(db_column="纤维/填充物", verbose_name="纤维/填充物", max_length=100)
    model_surface_temperature = FloatField(db_column="模具表面温度", verbose_name="模具表面温度", null=True, blank=True)
    melt_temperature = FloatField(db_column="熔体温度", verbose_name="熔体温度", null=True, blank=True)
    mold_temperature_range_min = FloatField(db_column="模具温度范围（最小值）", verbose_name="模具温度范围（最小值）", null=True, blank=True)
    mold_temperature_range_max = FloatField(db_column="模具温度范围（最大值）", verbose_name="模具温度范围（最大值）", null=True, blank=True)
    melt_temperature_range_min = FloatField(db_column="熔体温度范围（最小值）", verbose_name="熔体温度范围（最小值）", null=True, blank=True)
    melt_temperature_range_max = FloatField(db_column="熔体温度范围（最大值）", verbose_name="熔体温度范围（最大值）", null=True, blank=True)
    absolute_maximum_melt_temperature = FloatField(db_column="绝对最大溶体温度", verbose_name="绝对最大溶体温度", null=True, blank=True)
    ejection_temperature = FloatField(db_column="顶出温度", verbose_name="顶出温度", null=True, blank=True)
    maximum_shear_stress = FloatField(db_column="最大剪切应力", verbose_name="最大剪切应力", null=True, blank=True)
    maximum_shear_rate = FloatField(db_column="最大剪切速率", verbose_name="最大剪切速率", null=True, blank=True)
    melt_density = FloatField(db_column="熔体密度", verbose_name="熔体密度", null=True, blank=True)
    solid_density = FloatField(db_column="固体密度", verbose_name="固体密度", null=True, blank=True)
    pvt_b5 = FloatField(db_column="pvt-b5", verbose_name="pvt-b5", null=True, blank=True)
    pvt_b6 = FloatField(db_column="pvt-b6", verbose_name="pvt-b6", null=True, blank=True)
    pvt_b1m = FloatField(db_column="pvt-b1m", verbose_name="pvt-b1m", null=True, blank=True)
    pvt_b2m = FloatField(db_column="pvt-b2m", verbose_name="pvt-b2m", null=True, blank=True)
    pvt_b3m = FloatField(db_column="pvt-b3m", verbose_name="pvt-b3m", null=True, blank=True)
    pvt_b4m = FloatField(db_column="pvt-b4m", verbose_name="pvt-b4m", null=True, blank=True)
    pvt_b1s = FloatField(db_column="pvt-b1s", verbose_name="pvt-b1s", null=True, blank=True)
    pvt_b2s = FloatField(db_column="pvt-b2s", verbose_name="pvt-b2s", null=True, blank=True)
    pvt_b3s = FloatField(db_column="pvt-b3s", verbose_name="pvt-b3s", null=True, blank=True)
    pvt_b4s = FloatField(db_column="pvt-b4s", verbose_name="pvt-b4s", null=True, blank=True)
    pvt_b7 = FloatField(db_column="pvt-b7", verbose_name="pvt-b7", null=True, blank=True)
    pvt_b8 = FloatField(db_column="pvt-b8", verbose_name="pvt-b8", null=True, blank=True)
    pvt_b9 = FloatField(db_column="pvt-b9", verbose_name="pvt-b9", null=True, blank=True)
    elastic_modulus_e1 = FloatField(db_column="弹性模量E1", verbose_name="弹性模量E1", null=True, blank=True)
    elastic_modulus_e2 = FloatField(db_column="弹性模量E2", verbose_name="弹性模量E2", null=True, blank=True)
    poisson_ratio_v12 = FloatField(db_column="泊松比v12", verbose_name="泊松比v12", null=True, blank=True)
    poisson_ratio_v23 = FloatField(db_column="泊松比v23", verbose_name="泊松比v23", null=True, blank=True)
    shear_modulus_g12 = FloatField(db_column="剪切模量G12", verbose_name="剪切模量G12", null=True, blank=True)
    thermal_expansion_data_transverse_isotropic_coefficient_alpha1 = FloatField(db_column="热膨胀数据横向各向同性系数alpha1", verbose_name="热膨胀数据横向各向同性系数alpha1", null=True, blank=True)
    thermal_expansion_data_transverse_isotropic_coefficient_alpha2 = FloatField(db_column="热膨胀数据横向各向同性系数alpha2", verbose_name="热膨胀数据横向各向同性系数alpha2", null=True, blank=True)
    seven_params_n = FloatField(db_column="七参数n", verbose_name="七参数n", null=True, blank=True)
    seven_params_Tau = FloatField(db_column="七参数Tau*", verbose_name="七参数Tau*", null=True, blank=True)
    seven_params_D1 = FloatField(db_column="七参数D1", verbose_name="七参数D1", null=True, blank=True)
    seven_params_D2 = FloatField(db_column="七参数D2·", verbose_name="七参数D2·", null=True, blank=True)
    seven_params_D3 = FloatField(db_column="七参数D3", verbose_name="七参数D3", null=True, blank=True)
    seven_params_A1 = FloatField(db_column="七参数A1", verbose_name="七参数A1", null=True, blank=True)
    seven_params_A2 = FloatField(db_column="七参数A2", verbose_name="七参数A2", null=True, blank=True)
    c1 = FloatField(db_column="c1", verbose_name="c2", null=True, blank=True)
    c2 = FloatField(db_column="c2", verbose_name="c2", null=True, blank=True)
    conversion_temperature = FloatField(db_column="转换温度", verbose_name="转换温度", null=True, blank=True)
    MFR_temperature = FloatField(db_column="MFR温度", verbose_name="MFR温度", null=True, blank=True) 
    MFR_loading = FloatField(db_column="MFR载入", verbose_name="MFR载入", null=True, blank=True)
    measured_MFR = FloatField(db_column="测量的MFR", verbose_name="测量的MFR", null=True, blank=True)

    class Meta:
        db_table = "test"
        managed = False