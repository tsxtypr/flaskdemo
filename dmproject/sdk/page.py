import math
class Pager:

    def __init__(self,data,page_size):
        """

        :param data: 总数据
        :param page_size: 每页显示的条数
        """
        self.data = data
        self.page_size = page_size
        ## 是否有上一页
        self.has_previous_page = False
        ### 是否有下一页
        self.has_next_page = False

        ## 上一页
        self.previous_number = 0
        ## 下一页
        self.next_number = 0
        ## 总条数
        self.count = len(data)
        ## 最大页数
        self.num_pages = math.ceil(self.count/self.page_size)
        ### 页码范围
        self.page_range = (x for x in range(1,self.num_pages+1) )
    def page_data(self,page):
        """

        :return: 返回分页的数据
        """
        ## 是否有下一页
        if page != self.num_pages:
            self.has_next_page = True
            self.next_number = page+1
        ## 是否有上一页
        if page != 1:
            self.has_previous_page = True
            self.previous_number = page-1
        page_start = (page-1)*self.page_size ## 切片开始的位置
        page_end = page*self.page_size  ## 切片结束的位置
        result = self.data[page_start:page_end]
        return result