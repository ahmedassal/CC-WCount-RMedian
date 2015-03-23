from runningMedianCalculator import MedianCalculator

__author__ = 'Ahmed Assal'
import sys, os, datetime
import multiprocessing as mp
import tokenizers as toks
import runningMedianCalculator as med
import psutil

def schedulerV1(text):
    # if __name__ == '__main__':
        textPoolLength = len(text)
        # print(textPoolLength)
        # print(text[1])
        pool = mp.Pool(processes = textPoolLength)
        results = [pool.apply_async(toks.TokenizerV2, args=(x, text[x])) for x in range(textPoolLength)]
        output = [p.get() for p in results]

        # print(output)
        # jobs = []
        # for file_no in range(len(text_pool)):
        #     process = mp.Process(target= tokenizer, args = (file_no,))
        #     # tokenizer(file_no)
        #     jobs.append(process)
        #     print("scheduler ", file_no)
        #     process.start()
        #
        # for job in jobs:
        #     job.join()
        return output


def schedulerV2(path, *files):
    # if __name__ == '__main__':
        filesLength = len(files)
        # print(files)
        # manager = mp.Manager()
        pool = mp.Pool(processes=None)
        results = [pool.apply_async(toks.TokenizerV3, args=(x, files, path)) for x in range(filesLength)]
        output = [p.get() for p in results]
        # print(output)
        pool.close()
        pool.join()
        return output

def schedulerV3(text):
    # if __name__ == '__main__':
        textPoolLength = len(text)
        # print(textPoolLength)
        # print(text[1])
        pool = mp.Pool(processes = textPoolLength)
        results = [pool.apply_async(MedianCalculator, args=(x, text[x])) for x in range(textPoolLength)]
        output = [p.get() for p in results]
        print(output)
        pool.close()
        pool.join()
        return output

def dataLoaderV1(path, text):
    files = os.listdir(path)
    file_no = 0
    availableMem = psutil.virtual_memory().available
    memPerCPU = availableMem / cpusNum
    if (memPerCPU > memThreshold):
        memPerCPU = memThreshold

    print( "Available Memory = {0:0.0f}".format(availableMem/(1024**2)) + " MB,  Number of CPU Cores = " + str(cpusNum) + " cores, Estimated Memory Per CPU Core = {0:0.0f}".format(memPerCPU/(1024**2)) + " MB")
    filesTotalSize = 0
    filesSizes = []
    for file in files:
        print(path+file)
        filesSizes.append(os.path.getsize(path+file))
        filesTotalSize += filesSizes[file_no]
        file_no += file_no

    lines = ""
    linesSize = 0
    for file in files:
        try:
            f = open(path + str(file), "rU")
        except:
            print('Cannot open file %s for reading' % f)
            sys.exit(1)

        lineNo = 0
        for  line in f:
        #while (linesSize <memPerCPU):
            if(linesSize <memPerCPU):
                # line = f[lineNo]
                # pretext = re.match('', line)
                lines += line
                linesSize =sys.getsizeof(lines)
                # lineNo+=1
            else:
                text.append(lines)
                print(len(text))
                lines = ""
                linesSize = 0

        file_no += file_no
        f.close()

    return

def dataLoaderV2(path):
    files = os.listdir(path)
    return files

def dataLoaderV3(path, text):
    files = os.listdir(path)
    # print(files)
    file_no = 0
    files=sorted(files, key = lambda v: v, reverse=False)
    # print(files)
    lines = ""
    for file in files:
        try:
            f = open(path + str(file), "rU")
        except:
            print('Cannot open file %s for reading' % f)
            sys.exit(1)

        lineNo = 0
        txtFile = []

        for  line in f:
            txtFile.append(line)
            # lines += line
        text.append(txtFile)
        # text.append(lines)
        lines = ""
        f.close()

    return files