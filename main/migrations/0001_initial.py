

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilityName', models.CharField(max_length=255, unique=True)),
                ('facilityNo', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('completionDate', models.DateField(null=True)),
                ('landArea', models.CharField(max_length=255, null=True)),
                ('buildingArea', models.CharField(max_length=255, null=True)),
                ('totalBuildingArea', models.CharField(max_length=255, null=True)),
                ('highestHeight', models.CharField(max_length=255, null=True)),
                ('usage', models.CharField(max_length=255, null=True)),
                ('facilityStructure', models.CharField(max_length=255, null=True)),
                ('structuralForm', models.CharField(max_length=255, null=True)),
                ('amenities', models.CharField(max_length=255, null=True)),
                ('floors', models.CharField(max_length=255, null=True)),
                ('grade', models.CharField(max_length=255, null=True)),
                ('testResults', models.CharField(max_length=255, null=True)),
                ('plus', models.CharField(max_length=255, null=True)),
                ('frontView', models.ImageField(null=True, upload_to='images/frontView/%Y/%m/%d/')),
                ('locationMap', models.ImageField(null=True, upload_to='images/locationMap/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Crack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/crack_img/origin/%Y/%m/%d/')),
                ('flatting_image', models.ImageField(null=True, upload_to='images/crack_img/flatting/%Y/%m/%d/')),
                ('isFlattened', models.BooleanField(default=False)),
                ('originWidth', models.FloatField(null=True)),
                ('originHeight', models.FloatField(null=True)),
                ('crackLength', models.FloatField(null=True)),
                ('floor', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('absence', models.CharField(max_length=255, null=True)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('place', models.CharField(max_length=255, null=True)),
                ('number', models.CharField(max_length=255, null=True)),
                ('progress', models.CharField(max_length=255, null=True)),
                ('cause', models.CharField(max_length=255, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category')),
            ],
        ),
    ]
