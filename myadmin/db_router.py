# -*- coding: UTF-8 -*-
class appRouter(object):  # 配置app02的路由，去连接hvdb数据库
    """
    A router to control all database operations on models in the app02 application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read app02 models go to hvdb DB.
        """
        if model._meta.app_label == 'myadmin':  # app name（如果该app不存在，则无法同步成功）
            return 'guess'  # hvdb为settings中配置的database节点名称，并非db name。dbname为testdjango
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write app02 models go to hvdb DB.
        """
        if model._meta.app_label == 'myadmin':
            return 'guess'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app02 app is involved.
        当 obj1 和 obj2 之间允许有关系时返回 True ，不允许时返回 False ，或者没有 意见时返回 None 。
        """
        if obj1._meta.app_label == 'myadmin' or \
                        obj2._meta.app_label == 'myadmin':
            return True
        return None
    #
    # def allow_migrate(self, db, model):
    #     """
    #     Make sure the app02 app only appears in the hvdb database.
    #     """
    #     if db == 'guess':
    #         return model._meta.app_label == 'app02'
    #     elif model._meta.app_label == 'app02':
    #         return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
            if db == 'guess':
                return app_label == 'myadmin'
            elif app_label == 'myadmin':
                return False
            return None



    def allow_syncdb(self, db, model):  # 决定 model 是否可以和 db 为别名的数据库同步
        if db == 'guess' or model._meta.app_label == "myadmin":
            return False  # we're not using syncdb on our hvdb database
        else:  # but all other models/databases are fine
            return True
        return None