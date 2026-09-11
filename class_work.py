
def user_selected():
    print("!Обязательно!\nimport turtle as t <- в начале скрипта")
    print("Вставь сырой код: ")
    raw_code = input().lower().replace("[","")
    print("Вставь название переменной веса: ")
    weight = input()
    print("Вставь значение переменной веса: ")
    value_weight = input()
    print(rewriter(raw_code,value_weight,weight))
    
def rewriter(code: str, weight: int, name_weight:str) -> str:
    words = code.split()
    returned = f"{name_weight} = {weight}"
    end = False
    exit_from_loop = True
    next_i = 0
    
    while(end == False):
            if(next_i >= len(words) - 1):
                end = True
            for i in range(next_i, len(words)):
                if(exit_from_loop == False):   
                    match words[i].lower():
                        case "вперёд":
                            if "]" in words[i + 1]:
                                words[i + 1] = words[i + 1].replace("]","")
                                exit_from_loop = True
                                next_i = i + 1
                            returned += f"\n    t.forward({words[i + 1]} * {name_weight})"
                        case "налево":
                            if "]" in words[i + 1]:
                                words[i + 1] = words[i + 1].replace("]","")
                                exit_from_loop = True
                                next_i = i + 1
                            returned += f"\n    t.left({words[i + 1]})"
                        case "направо":
                            if "]" in words[i + 1]:
                                words[i + 1] = words[i + 1].replace("]","")
                                exit_from_loop = True
                                next_i = i + 1
                            returned += f"\n    t.right({words[i + 1]})"
                        case "назад":
                            if "]" in words[i + 1]:
                                words[i + 1] = words[i + 1].replace("]","")
                                exit_from_loop = True
                                next_i = i + 1
                            returned += f"\n    t.backward({words[i + 1]}  * {name_weight})"
                else:
                    break;
                            
            if(exit_from_loop == True):
                for i in range(next_i, len(words)):
                    match words[i].lower():
                        case "повтори":
                            returned += f"\nfor i in range({words[i + 1]}):"
                            exit_from_loop = False
                            next_i = i + 2
                            break;
                        case "вперёд":
                            returned += f"\nt.forward({words[i + 1]} * {weight})"
                        case "налево":
                            returned += f"\nt.left({words[i + 1]})"
                        case "направо":
                            returned += f"\nt.right({words[i + 1]})"
                        case "назад":
                            returned += f"\nt.backward({words[i + 1]}  * {weight})"
                        case "поднять":
                            returned += f"\nt.up()"
                        case "опустить":
                            returned += f"\nt.down()"
                        case "хвост":
                            continue
                    i += 1
    return "\n" + returned + "\n"