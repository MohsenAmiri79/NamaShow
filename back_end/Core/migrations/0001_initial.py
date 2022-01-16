# Generated by Django 3.2.5 on 2022-01-16 21:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('celebID', models.AutoField(primary_key=True, serialize=False)),
                ('nameOf', models.CharField(max_length=255)),
                ('gender', models.BooleanField(null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('nationality', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('filmID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('typeOf', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('numberOfFilminoRatings', models.PositiveIntegerField(default=0)),
                ('filminoRating', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('releaseDate', models.DateTimeField(null=True)),
                ('details', models.TextField()),
                ('salePercentage', models.PositiveIntegerField(default=0)),
                ('saleExpiration', models.DateTimeField(auto_now_add=True)),
                ('photoDirectory', models.TextField(null=True)),
                ('filmActor', models.ManyToManyField(related_name='actor', to='Core.Celebrity')),
                ('filmDirector', models.ManyToManyField(related_name='director', to='Core.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genreID', models.AutoField(primary_key=True, serialize=False)),
                ('nameOf', models.CharField(max_length=100, unique=True)),
                ('details', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postID', models.AutoField(primary_key=True, serialize=False)),
                ('adminID', models.PositiveIntegerField()),
                ('textOf', models.TextField()),
                ('dateOf', models.DateField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('saleID', models.AutoField(primary_key=True, serialize=False)),
                ('typeOf', models.IntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
                ('salePercentage', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subID', models.AutoField(primary_key=True, serialize=False)),
                ('nameOf', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('salePercentage', models.PositiveIntegerField(default=0)),
                ('saleExpiration', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(regex='^(?=[a-z0-9._]{5,20}$)(?!.*[_.]{2})[^_.].*[^_.]$')])),
                ('email', models.EmailField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('name', models.CharField(max_length=100)),
                ('isSuspended', models.BooleanField(default=False)),
                ('isAdmin', models.BooleanField(default=False)),
                ('emailActivation', models.BooleanField(default=False)),
                ('balance', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoID', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.PositiveIntegerField()),
                ('qualityHeight', models.PositiveIntegerField()),
                ('qualityWidth', models.PositiveIntegerField()),
                ('sizeOf', models.PositiveIntegerField()),
                ('episode', models.PositiveIntegerField(default=1)),
                ('season', models.PositiveIntegerField(default=1)),
                ('encoder', models.CharField(max_length=30)),
                ('directoryLocation', models.TextField()),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.film')),
            ],
        ),
        migrations.CreateModel(
            name='SubPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('dateOf', models.DateTimeField(auto_now_add=True)),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.subscription')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewID', models.AutoField(primary_key=True, serialize=False)),
                ('textOf', models.TextField()),
                ('dateOf', models.DateField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.film')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackingCode', models.PositiveIntegerField(default=0)),
                ('amount', models.PositiveIntegerField()),
                ('dateOf', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FilmPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('dateOf', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.film')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='filmGenre',
            field=models.ManyToManyField(to='Core.Genre'),
        ),
    ]
