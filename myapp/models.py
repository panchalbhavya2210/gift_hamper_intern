from django.db import models
from django.utils.safestring import mark_safe

class login_table(models.Model):
    Name = models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Password = models.CharField(max_length=20)
    dp = models.ImageField(upload_to="photos")
    Dob = models.DateField()
    Address = models.TextField()
    ROLE = (
        ("Vendor", "Vendor"),
        ("User", "User")
    )
    usertype = models.CharField(max_length=100, choices=ROLE, default="")
    is_verified = models.BooleanField(default=False)
    comments = models.CharField(max_length=100, default="")

    def customer_photos(self):
        return mark_safe('<img src ="{}" width ="100"/>'.format(self.dp.url))

    customer_photos.allow_tags = True

    def __str__(self):
        return self.Name


class product_category(models.Model):
    Product_category_name = models.CharField(max_length=25)
    Cat_image = models.ImageField(upload_to="photos",default="")

    def Cat_images(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Cat_image.url))

    Cat_images.allow_tags = True

    def __str__(self):
        return self.Product_category_name


class product_detail(models.Model):
    vendor_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    Pro_name = models.CharField(max_length=25)
    Pro_Cat = models.ForeignKey(product_category, on_delete=models.CASCADE, default="")
    Pro_image = models.ImageField(upload_to="photos")
    Pro_description = models.TextField()
    Pro_price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.Pro_name

    def Pro_images(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Pro_image.url))

    Pro_images.allow_tags = True



class hamper_details(models.Model):
    hamper_name = models.CharField(max_length=200)
    hamper_price = models.IntegerField()
    vendor_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    hamper_image = models.ImageField(upload_to="photos")
    is_active = models.BooleanField(default=True)

    def hamper_images(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.hamper_image.url))

    hamper_images.allow_tags = True

    def __str__(self):
        return self.hamper_name

class product_cart(models.Model):
    Product_id = models.ForeignKey(product_detail, on_delete=models.CASCADE, default="")
    L_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    Product_name = models.CharField(max_length=300)
    Date_time = models.DateTimeField(auto_now=True, editable=False)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Hamper_charge = models.IntegerField(default=0)
    Final_price = models.IntegerField()
    Order_id = models.IntegerField(default=0)
    Order_status = models.IntegerField(default=0)

class product_order(models.Model):
    Total_amount=models.IntegerField(default=0)
    L_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    Hamper_id = models.ForeignKey(hamper_details, on_delete=models.CASCADE, default="")
    Address=models.CharField(max_length=35)
    Order_status=(
        ('Pending','Pending'),
        ('Placed','Placed'),
    )
    order_status = models.CharField(max_length=50,choices=Order_status)
    Payment_status=models.CharField(max_length=30)
    Date_time=models.DateTimeField(auto_now=True, editable=False)

class contact(models.Model):
    Name=models.CharField(max_length=50,default="")
    Email=models.EmailField(default="")
    Comment=models.CharField(max_length=250,default="")


class FEEDBACK_TABLE(models.Model):
    L_ID = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    RATINGS = models.CharField(max_length=300)
    COMMENT = models.CharField(max_length=300, default="")

class hamper_feedback(models.Model):
    L_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    Hamper_id = models.ForeignKey(hamper_details, on_delete=models.CASCADE, default="")
    COMMENT = models.CharField(max_length=300, default="")
    Date_time = models.DateTimeField(auto_now=True, editable=False)

class product_review(models.Model):
    review_name = models.CharField(max_length=150, default='Default Review Name')
    user_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    p_id = models.ForeignKey(product_detail, on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.IntegerField()
    rev_image = models.ImageField(default='')
    submit_on = models.DateTimeField(auto_now=True)