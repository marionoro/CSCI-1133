def filter(infile,outfile):
    ifile = open(infile, 'r')
    ofile = open(outfile, 'w')
    for line in ifile:
        if line[:3] == 'The':
            ofile.write(line)
    ifile.close()
    ofile.close()
