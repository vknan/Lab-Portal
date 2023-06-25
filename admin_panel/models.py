from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        if not username:
            raise ValueError('The Username field must be set.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class Student(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)

    # Additional fields for authentication
    email_verified = models.BooleanField(default=False)
    mobile_verified = models.BooleanField(default=False)

    # Fields for Django authentication
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def _str_(self):
        return self.username

class CustomImage(models.Model):
    name = models.CharField(max_length=100)
    # Other fields for the custom image

    def _str_(self):
        return self.name

class VMSize(models.Model):
    name = models.CharField(max_length=100)
    # Other fields for the VM size

    def _str_(self):
        return self.name

class OSType(models.Model):
    name = models.CharField(max_length=100)
    # Other fields for the OS type

    def _str_(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    # Other fields for the region

    def _str_(self):
        return self.name

class VM(models.Model):
    VM_PROVIDERS = (
        ('AWS', 'Amazon Web Services'),
        ('Azure', 'Microsoft Azure'),
        ('Manual', 'Manually Added'),
    )

    VM_STATUS = (
        ('Active', 'Active'),
        ('Shutdown', 'Shutdown'),
    )

    LUNCHING_STATUS = (
        ('In Queue', 'In Queue'),
        ('Lunching', 'Lunching'),
        ('Getting Info', 'Getting Info'),
        ('Adding Final Touch', 'Adding Final Touch'),
        ('Almost Done', 'Almost Done'),
        ('Done', 'Done'),
    )

    OPRETION_STATUS = (
        ('Queued', 'Queued'),
        ('Performing Task', 'Performing Task'),
        ('Just There', 'Just There'),
        ('Done', 'Done'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    vm_id = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100)
    image = models.ForeignKey(CustomImage, on_delete=models.PROTECT)
    status = models.CharField(max_length=20)
    assigned_time = models.DateTimeField()
    launch_time = models.DateTimeField(null=True)
    expiry_time = models.DateTimeField(null=True)

    # Additional fields for VM provisioning
    vm_provider = models.CharField(max_length=10, choices=VM_PROVIDERS)
    vm_ip = models.CharField(max_length=100, blank=True)
    vm_password = models.CharField(max_length=100, blank=True)
    vm_size = models.ForeignKey(VMSize, on_delete=models.PROTECT)
    os_image = models.ForeignKey(OSType, on_delete=models.PROTECT)

    # Azure specific fields
    azure_nic = models.CharField(max_length=100, blank=True)
    azure_vnet = models.CharField(max_length=100, blank=True)

    # AWS specific fields
    aws_instance_id = models.CharField(max_length=100, blank=True)
    aws_subnet_id = models.CharField(max_length=100, blank=True)
    aws_security_group = models.CharField(max_length=100, blank=True)

    # Field for VM status
    is_active = models.BooleanField(default=False)

    # Additional fields
    is_created = models.BooleanField(default=False)
    lunching_status = models.CharField(max_length=20, choices=LUNCHING_STATUS, blank=True)
    is_operation = models.BooleanField(default=False)
    operation_status = models.CharField(max_length=20, choices=OPRETION_STATUS, blank=True)
    is_guacamole = models.BooleanField(default=False)
    guacamole_url = models.CharField(max_length=200, blank=True)
    guacamole_username = models.CharField(max_length=50, blank=True)
    guacamole_password = models.CharField(max_length=50, blank=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def _str_(self):
        return self.vm_id