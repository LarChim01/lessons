import sys
import inspect
from pprint import pprint



def introspection_info(obj):
    dict={}
    #тип объекта
    dict['type'] = str(type(obj))[:-1].split()[1][1:-1]
    #атрибуты объекта
    try :
        dict['attributes'] = obj.attribute
    except:
        dict['attributes'] = []
    #методы объекта
    dict['metod'] = dir(obj)
    #имя модуля
    dict['name']= __name__

    #версия Python
    dict['PyVer'] = sys.version.split()[0]
    #список импортированных модулей
    dict['moduls']= list(sys.modules.keys())

    return dict


number_info = introspection_info(42)
pprint(number_info)
