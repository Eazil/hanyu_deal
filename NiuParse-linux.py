import os


def excuteLtp(cmdline, inputFoler, outputFolder):
    n = 0
    for parents, folders, filenames in os.walk(inputFoler):
        for filename in filenames:
            inputFile = os.path.join(inputFoler, filename)
            outputFile = os.path.join(outputFolder, filename)
            if os.path.exists(outputFile)!=True:
                n+=1

                newCmdLine = cmdline + " -in " + inputFile + " -out " + outputFile
                os.system(newCmdLine)



if __name__ == '__main__':

    niuParserPath = r"H://NiuParser-v1.3.0-win//bin"
    model_exe = "//NiuParser-v1.3.0-mt-win.exe"
    model_action = [ " --POS "," --CP ", " --DP "]
    model_config = " -c niuparser.config "

    os.chdir(niuParserPath)


    # year = str(2015)
    # niuparseFolder = os.path.join("/home/nankang/Desktop/nianbao", "niuparser_" + year)
    # if os.path.exists(niuparseFolder):
    #     print("exists")
    # else:
    #     os.makedirs(niuparseFolder)

    # version = "version_" + "3"
    # fenlei = "v3_1"
    # input_pos_folder = os.path.join("/home/nankang/Desktop/cws", year+"_"+version+"_cws")
    # output_cws_folder = os.path.join(niuparseFolder, version + "_ws",fenlei)
    # input_pos_folder = output_cws_folder
    # output_pos_folder = os.path.join(niuparseFolder, version + "_pos")
    # input_cp_folder = input_pos_folder
    # output_cp_folder = os.path.join(niuparseFolder, version + "_cp")
    # input_dp_folder = input_pos_folder
    # output_dp_folder = os.path.join(niuparseFolder, version + "_dp")

    # if os.path.exists(output_cws_folder):
    #     print("exists")
    # else:
    #     os.mkdir(output_cws_folder)
    # if os.path.exists(output_pos_folder):
    #     print("exists")
    # else:
    #     os.makedirs(output_pos_folder)
    # if os.path.exists(output_cp_folder):
    #     print("exists")
    # else:
    #     os.makedirs(output_cp_folder)
    # if os.path.exists(output_dp_folder):
    #     print("exists")
    # else:
    #     os.makedirs(output_dp_folder)

        # cmdline = model_exe+threads_num+last_stage
    # cmdline_cws = "/home/hadoop1/desktop/NiuParser-v1.3.0-linux/bin/"+model_exe + model_action[0] + model_config
    cmdline_pos = niuParserPath+model_exe + model_action[0] + model_config
    cmdline_cp =  niuParserPath+model_exe + model_action[1] + model_config
    cmdline_dp =  niuParserPath+model_exe + model_action[2] + model_config
    # excuteLtp(cmdline_cws, input_cws_folder, output_cws_folder)
    # excuteLtp(cmdline_pos, input_pos_folder, output_pos_folder)
    # excuteLtp(cmdline_cp, input_cp_folder, output_cp_folder)
    # excuteLtp(cmdline_dp, input_dp_folder, output_dp_folder)
    # newCmdLine = cmdline + " -in " + inputFile + " -out " + outputFile
    inputFile='H://hanyu//hanyu_output_pos.txt'
    # file = open(inputFile,'r')
    # s = file.read()
    # print(s)
    # file.close()
    outputFile='H://hanyu//hanyu_output_dp.txt'
    # if os.path.exists(outputFile):
    #     print("exists")
    # else:
    #     os.makedirs(outputFile)
    # excuteLtp(cmdline_cp, inputFile, outputFile)
    newCmdLine=cmdline_dp+" -in " + inputFile + " -out " + outputFile
    os.system(newCmdLine)
