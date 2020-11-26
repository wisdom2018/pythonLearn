#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/7 5:27 PM
# @Author: zhangzhihui.wisdom
# @File:clickuse.py
import click


# python builtin Argparse standard library to create command line
# but it has some complexity in using aspect
# click compare Argparse more flexible
# use @click.command() to decorate a function,make it to be command line interface
# use @click.option() to decorate a function, can add command line option

@click.command()
# click.option() can use to add option parameter
@click.option('--count', default=1, help='Number of the greetings')
@click.option('--name', prompt='Your name', help='The person to greet')
# click.argument() can use to add constant parameter
@click.argument('coordinate')
# click.argument() has another usage, to accept variable parameters
# when nargs=-1 indicates that src can accept variable parameters.and also the parameter type is tuple
# when args>=1 indicates that can accept number of nargs parameter, for example the following example
@click.argument('src', nargs=-1)
@click.argument('dst', nagrs=1)
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello % s' % name)
        click.echo('coordinates %s' % coordinates)


# Group的使用
# Group通过group来创建一个命令行组


if __name__ == '__main__':
    hello()

# Options:
# --count INTEGER Number of greetings
# --name TEXT The person to greet
# --help show this message and exit
# python hello.py \
# --count 3
# --name Ethan
# --count=3
# --name=Ethan


