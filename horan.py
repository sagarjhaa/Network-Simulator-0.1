__author__ = 'sjha1'
# -*- coding: utf-8 -*-
"""
This code is used to calculte each user's attention.

Created on Fri Oct  2 21:31:19 2015

@author: Haoran-Sun
"""

#This code is still need to improved,
#for it only works for a single hashtag tweets.
#If a tweet has two or more hashtags, it consider the combination as a big hashtag


import csv
import math
from constants import *
#f=open("Short_Sample.csv")
#csv_f=csv.reader(f)
name=[]
dic={}

hashtags=[]
hashtag_cluster=[]

def read_file(text,directory):
    global name,dic,hastags,hashtag_cluster
    f=open(directory)
    csv_f=csv.reader(f)

    for row in csv_f:
        """
        Create two list for usernames and hashtags,
        and a list group hashtags of each tweets together
        """
        name.append(str(row[0]))
        hashtags.extend(row[1].split(','))
        hashtag_cluster.append(row[1].split())

    _main_(text)

# print(hashtags)
# print("/n")
# print(hashtag_cluster)


def init_dic(name):
    """
    create a dictionary, with username as the
    key and the # of apperearnce of hashtags  as value.
    No duplicate names here.
    """
    new_dic={}
    new_name=name
    name_set=set(new_name)
    for i in name_set:
        new_dic[i]=0
    return new_dic



def count(name,meme):
    """
    for each user, count the typical hashtags in their tweets
    the variable meme is the hashtag you want to search
    """
    namedic=init_dic(name)
    index=0

    for index in range(len(name)):

        if meme in hashtag_cluster[index]:
           #print(hashtag_cluster[index])
           namedic[name[index]]=namedic[name[index]]+1
           index+=1
    return namedic

#print(count(name,"Indian"))

#def sum_counts(dic):
#    """
#    get the total times of a meme emergence
#    ignore this function
#    """
#    sum=0
#    for key in dic:
#        sum=sum+dic[key]
#    return sum



def single_entropy_distribution(name,meme):
    """
    apply shannon entropy for a single meme for each user
    and gives a new dictionary
    subbtitute the counts of meme
    """
    new_dic=count(name,meme)
    for key in new_dic:
        tweets_amount=name.count(key)

        if(tweets_amount!=0) and (new_dic[key])!=0:
            #print math.log(float(new_dic[key])/tweets_amount,2)
            new_dic[key]=-(float(new_dic[key])/tweets_amount)*math.log(float(new_dic[key])/tweets_amount,2)

    return new_dic




def attentionOfUser(user):
    """
    calculate the breadth of attention for a user
    """
    global name,dic,hastags,hashtag_cluster

    attention=0
    i=0
    hashset=list(set(hashtags))
    for meme in hashset:
        attention=attention+single_entropy_distribution(name,meme)[user]

        i+=1
    return attention

def _main_(text):
    global name,dic,hastags,hashtag_cluster
    for each_user in list(set(name)):
        y = str(each_user) + " has attention:"
        x = attentionOfUser(each_user)
        string = str(y) + str(x)
        writeCalculations(text,string,False)

