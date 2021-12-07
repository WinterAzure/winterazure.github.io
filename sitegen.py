#!/bin/bash
from sys import argv
from random import shuffle
from subprocess import run
# This is a small tool to generate my small site

ARTICLE_CSS_MARKDOWN_BODY = '''
<style>
.markdown-body {
  background: linear-gradient(
    66deg,
    rgb(255, 68, 208) 0%,
    rgba(72, 255, 0, 0.849) 35%,
    rgb(241, 255, 51) 100%
  ) !important;
  border: #526980;
  margin: auto;
  width: 1024px;
  padding: 8px;
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
}
</style>
'''

BODY_BGCOLORS = ['<body bgcolor="green">', '<body bgcolor="yellow">', '<body bgcolor="blue">',
                '<body bgcolor="hotpink">', '<body bgcolor="pink">', '<body bgcolor="black">',
                '<body bgcolor="coral">', '<body bgcolor="cyan">', '<body bgcolor="hotpink">']

if len(argv)!=3:
    print('Invalid usage.\n')
    print('Usage: sitegen html_name html_title ')
    print('Use pandoc and special templet to generate html file from markdown,no space in arguments!')
    exit(1)

# insert css body
with open(argv[1],"a") as file:
    file.write(ARTICLE_CSS_MARKDOWN_BODY)
    shuffle(BODY_BGCOLORS)
    file.write(BODY_BGCOLORS[0])
    file.flush()

COMMAND_ARGS='6c '+'  <title>'+argv[2]+'</title>'
print('sed','-i',COMMAND_ARGS,argv[1])
run(['sed','-i',COMMAND_ARGS,argv[1]])

# copy file to /articles

run(['mv',argv[1],'./articles'])

# Update index.html
print('You need to update index.html !')

