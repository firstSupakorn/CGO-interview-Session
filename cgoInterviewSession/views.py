from django.http import HttpResponse
from rest_framework import generics


def get_queryset(request,x=0):
  try:
    x = int(request.GET.get('x'))
  except(ValueError, TypeError, AttributeError):
    return HttpResponse("Please enter the parameter-a in the form http://localhost:9999/testcgo/?x=1&a=1,2,3,4,5,7")

  try:
    a = request.GET.get('a')
    listA = a.split(",")
    listA = list(map(int, listA))
  except(ValueError, TypeError, AttributeError ):
    return HttpResponse("Please enter the parameter-a in the form http://localhost:9999/testcgo/?x=1&a=1,2,3,4,5,7")

  output = solution(x,listA)
  return HttpResponse("The earliest time when the frog can jump to the other side of the river is " + str(output))

def solution(X, A):

    numberOfElementList = [0] * len(A)
    uniqueList = [i for i in range(1,X+1)]

    if X > len(A):
        return -1

    for index,number in enumerate(A):
        if numberOfElementList[number-1] == 0:
            numberOfElementList[number-1] = numberOfElementList[number-1] + 1
            uniqueList.remove(number)

        if not uniqueList:
            return index

    if uniqueList:
        return -1
