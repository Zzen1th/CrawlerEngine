from domain.work import Domain
from elastic.work import Elastic
from host.work import Host


# �ɼ�ָ��
class Crawler(object):

    # ���캯��
    def __init__(self):
        super(Crawler, self).__init__()

    # ��ˮ��
    def start(self):
        # ����ɨ��
        Host().start()

        # ��ַָ��
        Elastic().startHost()

        # ����ɨ��
        Domain().start()

        # ��������
        Elastic().startSite()
