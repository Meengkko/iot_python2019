#  분산 저장 v1
#  빅데이터 수집부를 시뮬레이션 처리
import csv
import os

base_repository_name = 'Bigdata_Repository'
dir_delimeter = '/'
file_name = '시뮬레이션_서울특별시_관광지별_방문객'
file_format = 'csv'
initial_file_name = f'{base_repository_name}{dir_delimeter}{file_name}1.{file_format}'
simulation_count = 100
simulation_data = ['1111', '종로구', '서울특별시', '창덕궁', '1', '14137', '43677']
file_size_limit = 10000


def get_request_url():
    pass


def get_tour_point_visitor():
    pass


def get_tour_point_data(filewriter):
    filewriter.writerow(simulation_data)
    return


if not os.path.exists(base_repository_name):
    os.mkdir(base_repository_name)


def save_file(index):
    dest_file_name = f'{base_repository_name}{dir_delimeter}{file_name}{str(file_count())}.{file_format}'

    file_size = 0
    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"'{dest_file_name}' file size: {file_size}")
        print(f"파일당 size 제한: {file_size_limit}")
    except:
        pass

    csv_out_file = open(f'{base_repository_name}{dir_delimeter}{file_name}{str(index)}.{file_format}', 'a', newline='')
    filewriter = csv.writer(csv_out_file)
    header_list = ['addrCd', 'gungu', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
    filewriter.writerow(header_list)

    for index in range(simulation_count):
        get_tour_point_data(filewriter)
    csv_out_file.close()


def file_count():
    index = len(os.listdir(base_repository_name))
    return index


file_size = 0

if not os.path.exists(base_repository_name):
    os.mkdir(base_repository_name)

if not os.path.exists(initial_file_name):
    save_file(1)
else:
    save_file(file_count())
