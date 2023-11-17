from django.db import models
from django.conf import settings

# 적금 상품 목록
class DepositProducts(models.Model):
    # 상품 코드
    fin_prdt_cd = models.TextField(unique=True) 
    # 상품 이름
    fin_prdt_nm = models.TextField()         
    # 은행 이름
    kor_co_nm = models.TextField()              
    # 기타 유의 사항
    etc_note = models.TextField()               
    # 우대 조건
    spcl_cnd = models.TextField()   
    # 최대금리            
    mtrt_int = models.TextField()               
    # 가입 제한
    join_deny = models.IntegerField()           
    # 가입 대상
    join_member = models.TextField()            
    # 가입 방법
    join_way = models.TextField()               
   

# 적금 상품 옵션
class DepositOptions(models.Model):
    # 상품 코드
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete = models.CASCADE)
    # 저축 금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 기간
    save_trm = models.IntegerField(null=True)
    # 저축 금리
    intr_rate = models.FloatField(null=True)
    # 최대 우대 금리
    intr_rate2 = models.FloatField(null=True)


# 예금 상품 목록
class SavingProducts(models.Model):
    # 상품 코드
    fin_prdt_cd = models.TextField(unique=True) 
    # 상품 이름
    fin_prdt_nm = models.TextField()         
    # 은행 이름
    kor_co_nm = models.TextField()              
    # 기타 유의 사항
    etc_note = models.TextField()               
    # 우대 조건
    spcl_cnd = models.TextField()   
    # 최대금리            
    mtrt_int = models.TextField()               
    # 가입 제한
    join_deny = models.IntegerField()           
    # 가입 대상
    join_member = models.TextField()            
    # 가입 방법
    join_way = models.TextField()


# 예금 상품 옵션
class SavingOptions(models.Model):
    # 상품 코드
    fin_prdt_cd = models.ForeignKey(SavingProducts, on_delete = models.CASCADE)
    # 저축 금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 기간
    save_trm = models.IntegerField(null=True)
    # 저축 금리
    intr_rate = models.FloatField(null=True)
    # 최대 우대 금리
    intr_rate2 = models.FloatField(null=True)