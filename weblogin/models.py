# coding:utf-8
from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class UserInfo(models.Model):
    """
    用户信息表
    """
    uName = models.CharField("用户名", max_length=20)
    uPwd = models.CharField("密码", max_length=100)
    uEmail = models.EmailField("电子邮件")
    uPhone = models.DecimalField("手机号", max_digits=11, decimal_places=0)
    uAddr = models.CharField("收货地址", max_length=200)
    uTime = models.DateTimeField(auto_now_add=True)


class CharList(models.Model):
    """
    购物车表
    """
    cPrice = models.DecimalField("价格", max_digits=4, decimal_places=2)
    cNum = models.IntegerField("数量")
    cUser = models.ForeignKey('UserInfo', verbose_name="用户")
    cProduct = models.ForeignKey('ProductInfo', verbose_name="商品")


class OrderList(models.Model):
    """
    订单主表
    """
    oUser = models.ForeignKey('UserInfo')
    oSum = models.DecimalField("总价", max_digits=4, decimal_places=2)
    oTime = models.DateTimeField("订单生成时间", auto_now_add=True)
    oIspay = models.BooleanField("是否支付")


class Detailorder(models.Model):
    """
    订单从表
    """
    dProduct = models.ForeignKey('ProductInfo', verbose_name="商品")
    dNum = models.IntegerField("商品数量")
    dPrice = models.IntegerField("商品单价")
    dMain = models.ForeignKey('OrderList')


class ProductInfo(models.Model):
    """
    商品信息表
    """
    pName = models.CharField("商品名称", max_length=50)
    pPrice = models.DecimalField("商品单价", max_digits=4, decimal_places=2)
    pStock = models.IntegerField("库存")
    pDesc = models.CharField("商品介绍", max_length=1000)
    pDetail = HTMLField("商品详情")
    pTime_data = models.DateTimeField("商品添加时间", auto_now_add=True)
    pClass = models.ForeignKey('Sort')


class Sort(models.Model):
    """
    分类表
    """
    sClass = models.CharField(max_length=20)
