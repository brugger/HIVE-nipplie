#!/usr/bin/python
#
#
#
# Nick Gleadall contact: nick.gleadall@googlemail.com
# Kim Brugger contact: kim@brugger.dk

import sys
import pprint
import re
import os
pp = pprint.PrettyPrinter(indent=4)

hits  = dict()
genes = dict()

infile = sys.argv[1]

for i in os.listdir(infile):
   if not i.endswith("_hits.txt"):
     continue

#   print arg
   arg = i
   sample_name = arg
   sample_name = re.sub(r'(.*)_hits.txt', r'\1', sample_name)

#   print "--" + sample_name

   hits[ sample_name ] = dict()

#   pp.pprint(hits)

   fh = open(arg, 'r')
   header = fh.readline() #DEALS WITH HEADER LINE

   header_fields = header.split("\t");
   field_names = dict()
   for i in range(0, len(header_fields)):
       field_names[ header_fields[ i ]] = i

       pp.pprint( field_names )

   for line in fh:
       values = line.split("\t")

       #pp.pprint( values )

       gene_name      = values[ field_names['gene']]
       match_len_perc = values[ field_names['Percent id']]
       match_len_perc = "%.2f" %  float(match_len_perc)

       hits[ sample_name ][ gene_name ] = match_len_perc
       genes[ gene_name ] = 1


print ",".join(['Isolate'] + sorted(genes.keys()))

for sample_name in sorted(hits):

    line = []
    line.append( sample_name )
    for gene in sorted(genes.keys()):
        if ( gene not in hits[ sample_name ]):
          line.append("NA")
        else:
          line.append( hits[ sample_name ][ gene])

    print ",".join( line )
