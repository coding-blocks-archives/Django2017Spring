# Handler to create / alter or search through database written for JSON data
import json

DATA_DIR = './database/'
BASE_DATA = 'data.json'

def init_database():
	data = {
		'tables': {
			'INIT': {},
		}
	}
	f = open(DATA_DIR + BASE_DATA, 'r')
	d = f.read()
	f.close()
	if len(str(d)) < 2:
		f = open(DATA_DIR + BASE_DATA, 'w')
		f.write(json.dumps(data))
		f.close()
	else:
		pass

def create_table(table_name, **kwargs):
	f = open(DATA_DIR + BASE_DATA, 'r').read()
	data = json.loads(f)
	
	table = {
		'schema': kwargs
	}

	data['tables'][table_name] = table

	f = open(DATA_DIR + BASE_DATA, 'w')
	f.write(json.dumps(data))
	f.close()


def print_table():
	pass

def search():
	pass

def create_data():
	pass


if __name__ == '__main__':
	init_database()
	create_table('MyTable', name='varchar(10)', class_name='int', roll_no='int')