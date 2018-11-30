#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：hello.py

class Animal(object):
    def run(self):
        print 'Animal is running...'

    def run_twice(animal):
        animal.run()
        animal.run()


class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Dog Eating meat...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'

    def eat(self):
        print 'Cat Eating meat...'

b = Dog()
b.run()
