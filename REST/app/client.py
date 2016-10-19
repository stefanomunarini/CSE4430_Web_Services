import services

cc_number = 1234567890123456
amount = 10

arg = services.create_parser_arguments()

if __name__ == '__main__':

    keyword = arg.search
    if keyword:
        print(services.get_info(keyword))

    item_id = arg.buy
    if item_id:
        print(services.buy_product(cc_number, item_id))


    # args = sys.argv
    # if len(args) > 1:
    #     cc_number = args[1]
    # if len(args) > 2:
    #     amount = args[2]
    # print(test_bank_service(cc_number, amount))
