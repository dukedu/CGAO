from cgao.core.config import CONFIG


class ConfigService:

    @staticmethod
    def get(*keys):

        value = CONFIG

        for key in keys:

            value = value[key]

        return value