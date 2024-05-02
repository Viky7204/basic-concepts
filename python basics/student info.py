def student_info(**kwargs):              
  for key,value in kwargs.items():
    print(key+":"+value)
student_info(name="tasleem",age="20",clg="BITM")