from django.contrib import admin
from .models import (
    login_table,
    product_category,
    product_detail,
    hamper_details,
    product_cart,
    product_order,
    contact,
    FEEDBACK_TABLE,
    hamper_feedback,
    product_review
)

# Register your models here.

@admin.register(login_table)
class LoginTableAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Password','Phone', 'Dob', 'Address','customer_photos','usertype','is_verified','comments')
    search_fields = ['Name', 'Email']

@admin.register(product_category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('Product_category_name','Cat_images')
    search_fields = ['Product_category_name']

@admin.register(product_detail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('Pro_name', 'vendor_id', 'Pro_Cat', 'Pro_price','Pro_images','is_active')
    search_fields = ['Pro_name', 'vendor_id__Name', 'Pro_Cat__Product_category_name']


@admin.register(hamper_details)
class HamperDetailsAdmin(admin.ModelAdmin):
    list_display = ('hamper_name', 'hamper_price', 'vendor_id','hamper_images','is_active')
    search_fields = ['hamper_name', 'cat_id__hamper_category_name', 'vendor_id__Name']

@admin.register(product_cart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('Product_id', 'L_id', 'Product_name', 'Date_time', 'Price', 'Quantity', 'Hamper_charge', 'Final_price', 'Order_id', 'Order_status')
    search_fields = ['Product_name', 'L_id__Name', 'Hamper_id__hamper_name']

@admin.register(product_order)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('Total_amount', 'L_id', 'Hamper_id', 'Address', 'order_status', 'Payment_status', 'Date_time')
    search_fields = ['L_id__Name', 'Address']

@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Comment')
    search_fields = ['Name', 'Email']

@admin.register(FEEDBACK_TABLE)
class FeedbackTableAdmin(admin.ModelAdmin):
    list_display = ('L_ID', 'RATINGS', 'COMMENT')
    search_fields = ['L_ID__Name']

@admin.register(hamper_feedback)
class HamperFeedbackAdmin(admin.ModelAdmin):
    list_display = ('L_id', 'Hamper_id', 'COMMENT', 'Date_time')
    search_fields = ['L_id__Name', 'Hamper_id__hamper_name']
    
@admin.register(product_review)
class ProductReview(admin.ModelAdmin):
    list_display = ('review_name','user_id','p_id','comment','rating', 'rev_image','submit_on')
