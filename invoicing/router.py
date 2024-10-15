"Router Class used to link models with database"
class CarinaRouter:
    carine_db = "carina"
    default_db = "default"

    def db_for_read(self, model, **hints):
        model_name = model._meta.model_name
        if model_name == 'item':
            return self.carine_db
        else:
            return None

    def db_for_write(self, model, **hints):
        model_name = model._meta.model_name
        if model_name == 'item':
            raise Exception("This model is read only.")
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # if model_name == 'book':
        #     return db == 'books'
        # else:
            return db == 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'item' or \
                obj2._meta.app_label == 'item':
            return True
        elif 'item' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        return False