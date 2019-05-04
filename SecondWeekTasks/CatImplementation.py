import sys 
import os
import json


if __name__ == '__main__':
    json_obj = '''"settings" : {
  "serial"   : {serial},
  "version"  : {version}
}'''

    jsonParsed = json.loads(json_obj)

    print(jsonParsed['users'])
