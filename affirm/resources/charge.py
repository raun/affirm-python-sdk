from .base import Resource
from ..constants.url import URL


class Charge(Resource):
    def __init__(self, client=None):
        super(Charge, self).__init__(client)
        self.base_url = URL.CHARGE_URL

    def create(self, data={}, **kwargs):
        import pdb;pdb.set_trace()
        url = self.base_url
        self.post_url(url, data, **kwargs)

    def void(self, charge_id=None, **kwargs):
        url = "{}{}/void".format(self.base_url, charge_id)
        self.post_url(url, {}, **kwargs)

    def refund(self, charge_id=None, **kwargs):
        url = "{}{}/refund".format(self.base_url, charge_id)
        self.post_url(url, {}, **kwargs)

    def capture(self, charge_id=None, **kwargs):
        url = "{}{}/capture".format(self.base_url, charge_id)
        self.post_url(url, {}, **kwargs)

    def update(self, charge_id=None, **kwargs):
        url = "{}{}/update".format(self.base_url, charge_id)
        self.post_url(url, {}, **kwargs)
