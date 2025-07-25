# Generated by Django 4.2.15 on 2025-07-11 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnomalyDetectionDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('created_by', models.CharField(default='', max_length=32, verbose_name='Creator')),
                ('updated_by', models.CharField(default='', max_length=32, verbose_name='Updater')),
                ('domain', models.CharField(default='domain.com', max_length=100, verbose_name='Domain')),
                ('updated_by_domain', models.CharField(default='domain.com', max_length=100, verbose_name='updated by domain')),
                ('name', models.CharField(max_length=100, verbose_name='数据集名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='数据集描述')),
            ],
            options={
                'verbose_name': '异常检测数据集',
                'verbose_name_plural': '异常检测数据集',
            },
        ),
        migrations.CreateModel(
            name='DataPointFeaturesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('windows_size', models.IntegerField(default=30, help_text='滚动窗口大小', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='AnomalyDetectionTrainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('created_by', models.CharField(default='', max_length=32, verbose_name='Creator')),
                ('updated_by', models.CharField(default='', max_length=32, verbose_name='Updater')),
                ('domain', models.CharField(default='domain.com', max_length=100, verbose_name='Domain')),
                ('updated_by_domain', models.CharField(default='domain.com', max_length=100, verbose_name='updated by domain')),
                ('name', models.CharField(max_length=100, verbose_name='训练数据名称')),
                ('train_data', models.JSONField(help_text='存储训练数据', verbose_name='训练数据')),
                ('metadata', models.JSONField(blank=True, help_text='训练数据元信息', null=True, verbose_name='元数据')),
                ('is_train_data', models.BooleanField(default=False, help_text='是否为训练数据', verbose_name='是否为训练数据')),
                ('is_val_data', models.BooleanField(default=False, help_text='是否为验证数据', verbose_name='是否为验证数据')),
                ('is_test_data', models.BooleanField(default=False, help_text='是否为测试数据', verbose_name='是否为测试数据')),
                ('anomaly_point_count', models.PositiveIntegerField(default=0, help_text='异常点的数量', verbose_name='异常点数量')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='train_data', to='mlops.anomalydetectiondataset', verbose_name='数据集')),
            ],
            options={
                'verbose_name': '异常检测训练数据',
                'verbose_name_plural': '异常检测训练数据',
            },
        ),
        migrations.CreateModel(
            name='AnomalyDetectionTrainJob',
            fields=[
                ('datapointfeaturesinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mlops.datapointfeaturesinfo')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('created_by', models.CharField(default='', max_length=32, verbose_name='Creator')),
                ('updated_by', models.CharField(default='', max_length=32, verbose_name='Updater')),
                ('domain', models.CharField(default='domain.com', max_length=100, verbose_name='Domain')),
                ('updated_by_domain', models.CharField(default='domain.com', max_length=100, verbose_name='updated by domain')),
                ('name', models.CharField(max_length=100, verbose_name='任务名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='任务描述')),
                ('status', models.CharField(choices=[('pending', '待训练'), ('running', '训练中'), ('completed', '已完成'), ('failed', '训练失败')], default='pending', help_text='训练任务的当前状态', max_length=20, verbose_name='任务状态')),
                ('algorithm', models.CharField(choices=[('RandomForest', '随机森林')], help_text='使用的异常检测算法模型', max_length=50, verbose_name='算法模型')),
                ('hyperopt_config', models.JSONField(default=dict, help_text='用于超参数优化的配置参数', verbose_name='超参数优化配置')),
                ('max_evals', models.IntegerField(default=200, help_text='超参数优化的最大评估次数', verbose_name='最大评估次数')),
                ('test_data_id', models.ForeignKey(help_text='关联的异常检测测试数据集', on_delete=django.db.models.deletion.CASCADE, related_name='test_jobs', to='mlops.anomalydetectiontraindata', verbose_name='测试数据集')),
                ('train_data_id', models.ForeignKey(help_text='关联的异常检测训练数据集', on_delete=django.db.models.deletion.CASCADE, related_name='train_jobs', to='mlops.anomalydetectiontraindata', verbose_name='训练数据集')),
                ('val_data_id', models.ForeignKey(help_text='关联的异常检测验证数据集', on_delete=django.db.models.deletion.CASCADE, related_name='val_jobs', to='mlops.anomalydetectiontraindata', verbose_name='验证数据集')),
            ],
            options={
                'verbose_name': '异常检测训练任务',
                'verbose_name_plural': '异常检测训练任务',
            },
            bases=('mlops.datapointfeaturesinfo', models.Model),
        ),
        migrations.CreateModel(
            name='AnomalyDetectionServing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('created_by', models.CharField(default='', max_length=32, verbose_name='Creator')),
                ('updated_by', models.CharField(default='', max_length=32, verbose_name='Updater')),
                ('domain', models.CharField(default='domain.com', max_length=100, verbose_name='Domain')),
                ('updated_by_domain', models.CharField(default='domain.com', max_length=100, verbose_name='updated by domain')),
                ('name', models.CharField(help_text='服务的名称', max_length=100, verbose_name='服务名称')),
                ('description', models.TextField(blank=True, help_text='服务的详细描述', null=True, verbose_name='服务描述')),
                ('model_version', models.CharField(default='latest', help_text='模型版本', max_length=50, verbose_name='模型版本')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', help_text='服务的当前状态', max_length=20, verbose_name='服务状态')),
                ('anomaly_threshold', models.FloatField(default=0.5, help_text='用于判断异常的阈值', verbose_name='异常阈值')),
                ('anomaly_detection_train_job', models.ForeignKey(help_text='关联的异常检测训练任务模型ID', on_delete=django.db.models.deletion.CASCADE, related_name='servings', to='mlops.anomalydetectiontrainjob', verbose_name='模型ID')),
            ],
            options={
                'verbose_name': '异常检测服务',
                'verbose_name_plural': '异常检测服务',
                'ordering': ['-created_at'],
            },
        ),
    ]
