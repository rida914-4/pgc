# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Company(models.Model):
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    comp_name = models.CharField(max_length=100, blank=True, null=True)
    add_line1 = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    stax_no = models.CharField(max_length=17, blank=True, null=True)
    production = models.CharField(max_length=1, blank=True, null=True)
    clearing = models.CharField(max_length=1, blank=True, null=True)
    ke = models.CharField(max_length=1, blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    add_line2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.CharField(max_length=30, blank=True, null=True)
    acct_id_sh = models.CharField(max_length=10, blank=True, null=True)
    acct_id_sh_dr = models.CharField(max_length=10, blank=True, null=True)
    acct_id_pl = models.CharField(max_length=10, blank=True, null=True)
    bond = models.CharField(max_length=1, blank=True, null=True)
    clearance = models.CharField(max_length=1, blank=True, null=True)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    cur_name = models.CharField(max_length=10, blank=True, null=True)
    ship_dr = models.CharField(max_length=10, blank=True, null=True)
    ship_cr = models.CharField(max_length=10, blank=True, null=True)
    freight_dr = models.CharField(max_length=10, blank=True, null=True)
    freight_cr = models.CharField(max_length=10, blank=True, null=True)
    rickso_dr = models.CharField(max_length=10, blank=True, null=True)
    rickso_cr = models.CharField(max_length=10, blank=True, null=True)
    disc_dr = models.CharField(max_length=10, blank=True, null=True)
    disc_cr = models.CharField(max_length=10, blank=True, null=True)
    p_amt_cr = models.CharField(max_length=10, blank=True, null=True)
    cfs_cr = models.CharField(max_length=10, blank=True, null=True)
    permit_cr = models.CharField(max_length=10, blank=True, null=True)
    do_cr = models.CharField(max_length=10, blank=True, null=True)
    toll_cr = models.CharField(max_length=10, blank=True, null=True)
    agency_cr = models.CharField(max_length=10, blank=True, null=True)
    tpt_cr = models.CharField(max_length=10, blank=True, null=True)
    auction_dr = models.CharField(max_length=10, blank=True, null=True)
    inspection_dr = models.CharField(max_length=10, blank=True, null=True)
    auction_cr = models.CharField(max_length=10, blank=True, null=True)
    inspection_cr = models.CharField(max_length=10, blank=True, null=True)
    ken_dr = models.CharField(max_length=10, blank=True, null=True)
    ken_cr = models.CharField(max_length=10, blank=True, null=True)
    p_amt_to = models.CharField(max_length=10, blank=True, null=True)
    cfs_to = models.CharField(max_length=10, blank=True, null=True)
    permit_to = models.CharField(max_length=10, blank=True, null=True)
    do_to = models.CharField(max_length=10, blank=True, null=True)
    toll_to = models.CharField(max_length=10, blank=True, null=True)
    agency_to = models.CharField(max_length=10, blank=True, null=True)
    tpt_to = models.CharField(max_length=10, blank=True, null=True)
    stock_acct_id = models.CharField(max_length=10, blank=True, null=True)
    sales_acct_id = models.CharField(max_length=10, blank=True, null=True)
    debtors = models.CharField(max_length=10, blank=True, null=True)
    cogs = models.CharField(max_length=10, blank=True, null=True)
    comp_type = models.CharField(max_length=2, blank=True, null=True)
    track_ord = models.CharField(max_length=3, blank=True, null=True)
    grp_bs = models.CharField(max_length=1, blank=True, null=True)
    radiation_dr = models.CharField(max_length=10, blank=True, null=True)
    radiation_cr = models.CharField(max_length=10, blank=True, null=True)
    tt_acct_id = models.CharField(max_length=10, blank=True, null=True)
    er = models.FloatField(blank=True, null=True)
    country_flag = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Custodian(models.Model):
    acct_id = models.CharField(primary_key=True, max_length=4)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custodian'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Item(models.Model):
    stock_code = models.CharField(primary_key=True, max_length=10)
    description = models.CharField(max_length=100, blank=True, null=True)
    o_qty = models.FloatField(blank=True, null=True)
    specs = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=3, blank=True, null=True)
    o_rate = models.FloatField(blank=True, null=True)
    staxp = models.IntegerField(blank=True, null=True)
    cat_id = models.CharField(max_length=10, blank=True, null=True)
    inactive = models.CharField(max_length=2, blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Party(models.Model):
    acct_id = models.CharField(primary_key=True, max_length=7)
    acct_name = models.CharField(max_length=100, blank=True, null=True)
    add_line1 = models.CharField(max_length=50, blank=True, null=True)
    add_line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    ntn = models.CharField(max_length=50, blank=True, null=True)
    stax_no = models.CharField(max_length=20, blank=True, null=True)
    cnic = models.CharField(max_length=20, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    inactive = models.CharField(max_length=2, blank=True, null=True)
    gl_acct_id = models.CharField(max_length=10, blank=True, null=True)
    party_type = models.CharField(max_length=1, blank=True, null=True)
    old_acct_id = models.CharField(max_length=7, blank=True, null=True)
    del_day = models.CharField(max_length=10, blank=True, null=True)
    sp_id = models.CharField(max_length=7, blank=True, null=True)
    credit_days = models.IntegerField(blank=True, null=True)
    sms_no = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party'


class PlInvoice(models.Model):
    voucher_id = models.CharField(primary_key=True, max_length=10)
    voucher_date = models.DateField(blank=True, null=True)
    acct_id = models.CharField(max_length=4, blank=True, null=True)
    net_amt = models.FloatField(blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    posted = models.CharField(max_length=2, blank=True, null=True)
    pos_code = models.CharField(max_length=10, blank=True, null=True)
    cust_id = models.CharField(max_length=4, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_invoice'


class PlInvoicedet(models.Model):
    voucher = models.ForeignKey(PlInvoice, models.DO_NOTHING)
    lineitem = models.CharField(max_length=6)
    stock_code = models.CharField(max_length=13, blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    itemtot = models.FloatField(blank=True, null=True)
    emp_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_invoicedet'
        unique_together = (('voucher', 'lineitem'),)


class Positions(models.Model):
    pos_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'positions'


class Reports(models.Model):
    file_name = models.CharField(max_length=50)
    report_name = models.CharField(max_length=100)
    cat = models.BooleanField()
    landscape = models.CharField(max_length=1)
    rep_id = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'reports'


class StkCat(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=6)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'stk_cat'




class Users(models.Model):
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    emp_name = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    auth_id = models.CharField(max_length=1, blank=True, null=True)
    use_form = models.CharField(max_length=1, blank=True, null=True)
    use_rep = models.CharField(max_length=1, blank=True, null=True)
    logged = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    chasis_no = models.CharField(max_length=50, blank=True, null=True)
    pk_bill_no_from = models.CharField(max_length=4, blank=True, null=True)
    pk_bill_no_to = models.CharField(max_length=4, blank=True, null=True)
    usd = models.CharField(max_length=1, blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    voucher_type = models.CharField(max_length=2, blank=True, null=True)
    post = models.CharField(max_length=1, blank=True, null=True)
    sp_id = models.CharField(max_length=4, blank=True, null=True)
    u_session_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

# class for view v_pl_invoice
# CREATE OR REPLACE FORCE VIEW "PGC_AM"."V_PL_INVOICE" ("VOUCHER_ID", "VOUCHER_DATE", "DESCRIPTION", "POS_NAME", "CUST_NAME") AS
#   SELECT DISTINCT m.voucher_id, m.voucher_date ,i.description, p.description pos_name, c.description cust_name
# FROM PL_INVOICE m
# LEFT JOIN PL_INVOICEDET d ON m.voucher_id = d.voucher_id
# LEFT JOIN positions p ON m.pos_code=p.pos_code
# LEFT JOIN custodian c ON m.cust_id=c.acct_id
# LEFT JOIN item i ON m.acct_id=i.stock_code
# WHERE 1=1


class VPlInvoice(models.Model):
    voucher_id = models.CharField(primary_key=True, max_length=10)
    voucher_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    pos_name = models.CharField(max_length=100, blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    acct_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_pl_invoice'


# CREATE OR REPLACE FORCE VIEW "PGC_AM"."V_PL_INVOICEDET" ("ID", "VOUCHER_ID", "VOUCHER_DATE", "ACCT_ID", "NET_AMT", "PARTICULARS", "POST_DATE", "ADDRESS", "POSTED", "POS_CODE", "CUST_ID", "POS_NAME", "CUST_NAME", "STOCK_CODE", "STOCK_NAME") AS
#   SELECT
# v."ID",v."VOUCHER_ID",v."VOUCHER_DATE",v."ACCT_ID",v."NET_AMT",v."PARTICULARS",v."POST_DATE",v."ADDRESS",v."POSTED",v."POS_CODE",v."CUST_ID", p.description pos_name, c.description cust_name,
# d.stock_code,
# i.description stock_name
# FROM pl_invoice v, PL_INVOICEDET d, item i , positions p, custodian c
# where v.voucher_id = d.voucher_id
# and v.acct_id = i.stock_code
# and v.pos_code=p.pos_code
# and v.cust_id=c.ACCT_ID


class VPlInvoicedet(models.Model):
    voucher_id = models.CharField(max_length=10, blank=True, null=True, primary_key=True)
    voucher_date = models.DateField(blank=True, null=True)
    acct_id = models.CharField(max_length=4, blank=True, null=True)
    net_amt = models.FloatField(blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    posted = models.CharField(max_length=2, blank=True, null=True)
    pos_code = models.CharField(max_length=10, blank=True, null=True)
    cust_id = models.CharField(max_length=4, blank=True, null=True)
    pos_name = models.CharField(max_length=100, blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    stock_code = models.CharField(max_length=13, blank=True, null=True)
    stock_name = models.CharField(max_length=100, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    component_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_pl_invoicedet'

    # def __str__(self):
    #     return self.voucher_id, self.voucher_date


class Question(models.Model):
    question = models.TextField(blank=True)
    answered = models.BooleanField