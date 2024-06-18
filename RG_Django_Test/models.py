# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcfCacheAds(models.Model):
    id = models.BigAutoField(primary_key=True)
    ads_id = models.BigIntegerField()
    ads_content = models.TextField(null=True)
    ads_position = models.CharField(max_length=100)
    ads_order = models.IntegerField()
    ads_filter = models.CharField(max_length=100)
    filter_item = models.CharField(max_length=100)
    f2_post_condition = models.IntegerField()
    f2_post = models.TextField(null=True)
    f2_company_condition = models.IntegerField()
    f2_company = models.TextField(null=True)
    f2_category_condition = models.IntegerField()
    f2_category = models.TextField(null=True)
    f2_tag_condition = models.IntegerField()
    f2_tag = models.TextField(null=True)
    f2_state_condition = models.IntegerField()
    f2_state = models.TextField(null=True)
    f2_zip_condition = models.IntegerField()
    f2_zip = models.TextField(null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'acf_cache_ads'


class Ads(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    ads_content = models.TextField(null=True)
    ads_position = models.CharField(max_length=100)
    ads_order = models.IntegerField()
    ads_contact_enable = models.IntegerField()
    ads_contact_send_to = models.CharField(max_length=200)
    author = models.BigIntegerField()
    post_status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'ads'


class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    content = models.TextField(null=True)
    excerpt = models.TextField(null=True)
    author = models.BigIntegerField()
    meta_title = models.TextField(null=True)
    meta_description = models.TextField(null=True)
    meta_keywords = models.TextField(null=True)
    featured_image = models.TextField(null=True)
    post_status = models.CharField(max_length=50)
    comment_status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'blog'


class BlogCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)
    image = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'blog_category'


class BlogCategoryLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'blog_category_link'
        unique_together = (('blog_id', 'category_id'),)


class BlogTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)
    image = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'blog_tag'


class BlogTagLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.BigIntegerField()
    tag_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'blog_tag_link'
        unique_together = (('blog_id', 'tag_id'),)


class Customers(models.Model):
    invoice_num = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    plan_id = models.CharField(max_length=100, blank=True, null=True)
    subscription_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'customers'


class FormEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.CharField(max_length=250)
    form_entries = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'form_entries'


class Orders(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    status = models.TextField(null=Trueblank=True, null=True)  # This field type is a guess.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    url = models.CharField(db_column='Url', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'orders'


class Plans(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    features = models.CharField(max_length=355, blank=True, null=True)
    product_pid = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'plans'


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    content = models.TextField(null=True)
    excerpt = models.TextField(null=True)
    author = models.BigIntegerField()
    meta_title = models.TextField(null=True)
    meta_description = models.TextField(null=True)
    meta_keywords = models.TextField(null=True)
    featured_image = models.TextField(null=True)
    add_company = models.BigIntegerField()
    add_keywords = models.TextField(null=True)
    add_tag_line = models.TextField(null=True)
    add_website = models.TextField(null=True)
    add_phone = models.TextField(null=True)
    add_contact_email = models.TextField(null=True)
    add_owner = models.TextField(null=True)
    add_submitter_email = models.TextField(null=True)
    add_submitter_phone = models.TextField(null=True)
    add_keyword_1 = models.TextField(null=True)
    add_keyword_2 = models.TextField(null=True)
    add_keyword_3 = models.TextField(null=True)
    add_overview = models.TextField(null=True)
    addr_full_address = models.TextField(null=True)
    addr_address_1 = models.TextField(null=True)
    addr_address_2 = models.TextField(null=True)
    addr_address_3 = models.TextField(null=True)
    addr_city = models.CharField(max_length=100)
    addr_state = models.CharField(max_length=100)
    addr_zip = models.CharField(max_length=10)
    addr_county = models.CharField(max_length=100)
    addr_latitude = models.CharField(max_length=10)
    addr_longitude = models.CharField(max_length=10)
    addr_other_state = models.CharField(max_length=100)
    addr_country = models.CharField(max_length=100)
    tab_overview = models.TextField(null=True)
    tab_location = models.TextField(null=True)
    tab_reviews = models.TextField(null=True)
    tab_hours_monday = models.CharField(max_length=50)
    tab_hours_tuesday = models.CharField(max_length=50)
    tab_hours_wednesday = models.CharField(max_length=50)
    tab_hours_thursday = models.CharField(max_length=50)
    tab_hours_friday = models.CharField(max_length=50)
    tab_hours_saturday = models.CharField(max_length=50)
    tab_hours_sunday = models.CharField(max_length=50)
    tab_buynow_button_text = models.CharField(max_length=250)
    tab_buynow_outgoing_url = models.CharField(max_length=250)
    tab_buynow_background_color = models.CharField(max_length=10)
    tab_buynow_text_color = models.CharField(max_length=10)
    tab_buynow_triggered_event = models.CharField(max_length=50)
    icon_link_url = models.CharField(max_length=250)
    icon_link_follow = models.CharField(max_length=50)
    icon_link_target = models.CharField(max_length=50)
    icon_link_image_alt = models.CharField(max_length=250)
    background_header = models.CharField(max_length=250)
    shop_url = models.CharField(max_length=250)
    disable_adsense = models.IntegerField()
    show_contact_form = models.IntegerField()
    claim_status = models.IntegerField()
    post_status = models.CharField(max_length=50)
    comment_status = models.CharField(max_length=50)
    wp_category_link = models.IntegerField()
    wp_tag_link = models.IntegerField()
    wp_reviews = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile'


class ProfileCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)
    category_2 = models.CharField(max_length=255)
    category_3 = models.CharField(max_length=255)
    image = models.CharField(max_length=250)
    thumbtack_id = models.CharField(max_length=255)
    thumbtack_name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_category'


class ProfileCategoryLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_category_link'


class ProfileCategoryLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country_slug = models.CharField(max_length=100)
    state_slug = models.CharField(max_length=100)
    city_slug = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_category_location'


class ProfileCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    disable_ads_on_profiles = models.IntegerField()
    reviews_layout = models.CharField(max_length=50)
    reviews_page_title = models.CharField(max_length=255)
    reviews_content = models.TextField(null=True)
    reviews_meta_description = models.CharField(max_length=255)
    reviews_meta_keywords = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    google = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_company'


class ProfileCounty(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_county'


class ProfileState(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    image_mobile = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_state'


class ProfileTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_tag'


class ProfileTagLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_id = models.BigIntegerField()
    tag_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profile_tag_link'
        unique_together = (('profile_id', 'tag_id'),)


class Profiletest(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    content = models.TextField(null=True)
    excerpt = models.TextField(null=True)
    author = models.BigIntegerField()
    meta_title = models.TextField(null=True)
    meta_description = models.TextField(null=True)
    meta_keywords = models.TextField(null=True)
    featured_image = models.TextField(null=True)
    add_company = models.BigIntegerField()
    add_keywords = models.TextField(null=True)
    add_tag_line = models.TextField(null=True)
    add_website = models.TextField(null=True)
    add_phone = models.TextField(null=True)
    add_contact_email = models.TextField(null=True)
    add_owner = models.TextField(null=True)
    add_submitter_email = models.TextField(null=True)
    add_submitter_phone = models.TextField(null=True)
    add_keyword_1 = models.TextField(null=True)
    add_keyword_2 = models.TextField(null=True)
    add_keyword_3 = models.TextField(null=True)
    add_overview = models.TextField(null=True)
    addr_full_address = models.TextField(null=True)
    addr_address_1 = models.TextField(null=True)
    addr_address_2 = models.TextField(null=True)
    addr_address_3 = models.TextField(null=True)
    addr_city = models.CharField(max_length=100)
    addr_state = models.CharField(max_length=100)
    addr_zip = models.CharField(max_length=10)
    addr_county = models.CharField(max_length=100)
    addr_latitude = models.CharField(max_length=10)
    addr_longitude = models.CharField(max_length=10)
    addr_other_state = models.CharField(max_length=100)
    addr_country = models.CharField(max_length=100)
    tab_overview = models.TextField(null=True)
    tab_location = models.TextField(null=True)
    tab_reviews = models.TextField(null=True)
    tab_hours_monday = models.CharField(max_length=50)
    tab_hours_tuesday = models.CharField(max_length=50)
    tab_hours_wednesday = models.CharField(max_length=50)
    tab_hours_thursday = models.CharField(max_length=50)
    tab_hours_friday = models.CharField(max_length=50)
    tab_hours_saturday = models.CharField(max_length=50)
    tab_hours_sunday = models.CharField(max_length=50)
    tab_buynow_button_text = models.CharField(max_length=250)
    tab_buynow_outgoing_url = models.CharField(max_length=250)
    tab_buynow_background_color = models.CharField(max_length=10)
    tab_buynow_text_color = models.CharField(max_length=10)
    tab_buynow_triggered_event = models.CharField(max_length=50)
    icon_link_url = models.CharField(max_length=250)
    icon_link_follow = models.CharField(max_length=50)
    icon_link_target = models.CharField(max_length=50)
    icon_link_image_alt = models.CharField(max_length=250)
    background_header = models.CharField(max_length=250)
    shop_url = models.CharField(max_length=250)
    disable_adsense = models.IntegerField()
    show_contact_form = models.IntegerField()
    claim_status = models.IntegerField()
    post_status = models.CharField(max_length=50)
    comment_status = models.CharField(max_length=50)
    wp_category_link = models.IntegerField()
    wp_tag_link = models.IntegerField()
    wp_reviews = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'profiletest'


class Redirections(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(unique=True, max_length=255)
    target = models.CharField(max_length=255)
    rtype = models.CharField(max_length=5)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'redirections'


class Settings(models.Model):
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    key = models.CharField(max_length=255)
    value = models.TextField(null=Trueblank=True, null=True)
    type = models.CharField(max_length=31)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'settings'


class UpdateLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    table_id = models.BigIntegerField()
    previous = models.JSONField()
    updated_by = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'update_log'


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
