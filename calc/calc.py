# -*- coding: utf-8 -*-
from cgi import parse_qs
from template import html

def application(environ, start_response):
        d = parse_qs(environ['QUERY_STRING'])
        first_num = d.get('first_num', [''])[0]
        second_num = d.get('second_num', [''])[0]
        sum, mul = "enter two numbers", "enter two numbers" 
        try:
                first_num, second_num = int(first_num), int(second_num)
	except ValueError:
		if first_num.isdigit():	
			error = "you entered wrong value in first_num"
			sum=-1
			mul=-1
		elif second_num.isdigit():
			error = "you entered wrong value in second_num"
			sum=-1
			mul=-1
		else:
			error = "you entered the wrong value"		
	else:
		error=""        
	        sum = first_num + second_num
                mul = first_num * second_num


        response_body = html % {'sum' : sum, 'mul' : mul,'error' : error }


        start_response ('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]

