import math

class Paginator:
    """
    通过切片进行分页

    提供分页的功能
    """
    def __init__(self,data,page_size):
        """

        :param data:  数据
        :param page_size: 每页条数
        """
        self.data=data
        self.page_size=page_size
        self.is_start=False
        self.is_end=False
        self.page_count=len(self.data)
        self.privious_page=0
        self.next_page=0
        self.page_number=math.ceil(len(self.data)/self.page_size)   #总页数
        self.page_range=(x for x in range(1,self.page_number+1))    #迭代器   页数范围
    def page_data(self,page):
        # 返回分页的数据
        start=(page-1)*self.page_size
        end=page*self.page_size
        result=self.data[start:end]
        if page==1:
            print('-----')
            self.is_start=True
        if page==self.page_number:
            self.is_end=True
        self.next_page=page+1
        self.privious_page=page-1
        return result

from models import LoginUser

if __name__ == '__main__':
    params=LoginUser.query.all()  #列表
    paginator=Paginator(params,5)
    print(paginator.page_size)
    print(paginator.data)
    print(paginator.page_number)
    print(paginator.page_range)
    print(paginator.page_count)
    print(paginator.is_start)
    print(paginator.is_end)
    print(paginator.next_page)
    print(paginator.privious_page)
