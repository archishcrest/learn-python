from django.db import models

# Create your models here.



class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(null=True,max_length=250)
    slug = models.CharField(null=True,max_length=250)
    content = models.TextField(null=True)
    excerpt = models.TextField(null=True)
    author = models.BigIntegerField(null=True)
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
    addr_city = models.CharField(null=True,max_length=100)
    addr_state = models.CharField(null=True,max_length=100)
    addr_zip = models.CharField(null=True,max_length=10)
    addr_county = models.CharField(null=True,max_length=100)
    addr_latitude = models.CharField(null=True,max_length=10)
    addr_longitude = models.CharField(null=True,max_length=10)
    addr_other_state = models.CharField(null=True,max_length=100)
    addr_country = models.CharField(null=True,max_length=100)
    tab_overview = models.TextField(null=True)
    tab_location = models.TextField(null=True)
    tab_reviews = models.TextField(null=True)
    tab_hours_monday = models.CharField(null=True,max_length=50)
    tab_hours_tuesday = models.CharField(null=True,max_length=50)
    tab_hours_wednesday = models.CharField(null=True,max_length=50)
    tab_hours_thursday = models.CharField(null=True,max_length=50)
    tab_hours_friday = models.CharField(null=True,max_length=50)
    tab_hours_saturday = models.CharField(null=True,max_length=50)
    tab_hours_sunday = models.CharField(null=True,max_length=50)
    tab_buynow_button_text = models.CharField(null=True,max_length=250)
    tab_buynow_outgoing_url = models.CharField(null=True,max_length=250)
    tab_buynow_background_color = models.CharField(null=True,max_length=10)
    tab_buynow_text_color = models.CharField(null=True,max_length=10)
    tab_buynow_triggered_event = models.CharField(null=True,max_length=50)
    icon_link_url = models.CharField(null=True,max_length=250)
    icon_link_follow = models.CharField(null=True,max_length=50)
    icon_link_target = models.CharField(null=True,max_length=50)
    icon_link_image_alt = models.CharField(null=True,max_length=250)
    background_header = models.CharField(null=True,max_length=250)
    shop_url = models.CharField(null=True,max_length=250)
    disable_adsense = models.IntegerField(null=True)
    show_contact_form = models.IntegerField(null=True)
    claim_status = models.IntegerField()
    post_status = models.CharField(null=True,max_length=50)
    comment_status = models.CharField(null=True,max_length=50)
    wp_category_link = models.IntegerField(null=True)
    wp_tag_link = models.IntegerField(null=True)
    wp_reviews = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile'


class ProfileCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=True,max_length=255)
    slug = models.CharField(unique=True, null=True,max_length=255)
    description = models.TextField(null=True)
    category_2 = models.CharField(null=True,max_length=255)
    category_3 = models.CharField(null=True,max_length=255)
    image = models.CharField(null=True,max_length=250)
    thumbtack_id = models.CharField(null=True,max_length=255)
    thumbtack_name = models.CharField(null=True,max_length=255)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_category'


class ProfileCategoryLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE,db_column='profile_id')
    category_id = models.ForeignKey('ProfileCategory', on_delete=models.CASCADE,db_column='category_id')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_category_link'


class ProfileCategoryLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey('ProfileCategory', on_delete=models.CASCADE,db_column='category_id')
    country = models.CharField(null=True,max_length=50)
    state = models.CharField(null=True,max_length=50)
    city = models.CharField(null=True,max_length=100)
    country_slug = models.CharField(null=True,max_length=100)
    state_slug = models.CharField(null=True,max_length=100)
    city_slug = models.CharField(null=True,max_length=100)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_category_location'


class ProfileCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=True,max_length=255)
    slug = models.CharField(null=True,max_length=255)
    disable_ads_on_profiles = models.IntegerField()
    reviews_layout = models.CharField(null=True,max_length=50)
    reviews_page_title = models.CharField(null=True,max_length=255)
    reviews_content = models.TextField(null=True)
    reviews_meta_description = models.CharField(null=True,max_length=255)
    reviews_meta_keywords = models.CharField(null=True,max_length=255)
    facebook = models.CharField(null=True,max_length=255)
    twitter = models.CharField(null=True,max_length=255)
    instagram = models.CharField(null=True,max_length=255)
    google = models.CharField(null=True,max_length=255)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_company'


class ProfileCounty(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(null=True,max_length=50)
    county = models.CharField(null=True,max_length=100)
    url = models.CharField(null=True,max_length=250)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_county'


class ProfileState(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=True,max_length=250)
    image = models.CharField(null=True,max_length=250)
    image_mobile = models.CharField(null=True,max_length=250)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_state'


class ProfileTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=True,max_length=255)
    slug = models.CharField(unique=True, null=True,max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_tag'


class ProfileTagLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_id = models.BigIntegerField()
    tag_id = models.BigIntegerField()
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        #managed = False
        db_table = 'profile_tag_link'
        unique_together = (('profile_id', 'tag_id'),)

