def error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"    
        case 418:
            return "I'm Teaport"    
        case _:
            return "Somethings wrong with the internet"    