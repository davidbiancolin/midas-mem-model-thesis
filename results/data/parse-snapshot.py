#!/usr/bin/env python

import optparse

def read_snapshot(filename):
  reg_count = 0
  sram_count = 0
  deltaTable = dict()
  valueTable = dict()
  with open(filename, 'r') as f:
    for line in f:
      tokens = line.split()
      if tokens[0] == '0':
        if tokens[1] == '1':
          if "lastCycle" in tokens[2]:
            lastCycle_id = reg_count
          elif "overflow" in tokens[2]:
            overflow_id = reg_count
          elif "head" in tokens[2]:
            head_id = reg_count
          elif "null" in tokens[2]:
            pass
          reg_count += 1
        elif tokens[1] == '2':
          if "valueTable" in tokens[2]:
            valueTable_id = sram_count
          elif "deltaTable" in tokens[2]:
            deltaTable_id = sram_count
          sram_count +=1
      elif tokens[0] == '1':
        # Cycle
        pass
      elif tokens[0] == '2':
        # Snapshot
        if tokens[1] == '1':
          if int(tokens[2]) == lastCycle_id:
            lastCycle = int(tokens[3], 16)
          elif int(tokens[2]) == overflow_id:
            overflow = int(tokens[3], 16)
          elif int(tokens[2]) == head_id:
            head = int(tokens[3], 16)
        elif tokens[1] == '2':
          if int(tokens[2]) == valueTable_id:
            valueTable[int(tokens[4])] = int(tokens[3], 16)
          elif int(tokens[2]) == deltaTable_id:
            deltaTable[int(tokens[4])] = int(tokens[3], 16)
        else:
          assert False
      else:
        assert False

  return lastCycle, head, overflow, deltaTable, valueTable


def parse_data(lastCycle, head, overflow, deltaTable, valueTable):
  print "overflow:", overflow
  print "head:", head

  delta = None
  deltaSum = 0
  tableSize = 2 ** 17
  pointer = head
  isAddress = False
  series = list() # (delta, size, addr)

  while True:
    deltaSum += deltaTable[pointer]
    if valueTable[pointer] < 0x10000000:
      isAddress = False
    else:
      isAddress = True

    if not isAddress:
      delta = deltaTable[pointer]
      size = valueTable[pointer]
      isAddress = True
    else:
      if delta:
        series.append((delta, size, deltaTable[pointer], valueTable[pointer]))
      isAddress = False
    pointer += 1
    if pointer == tableSize:
      pointer = 0
    if pointer == head:
      break

  baseCycle = lastCycle - deltaSum
  print "base cycle:", baseCycle
  for delta1, size, delta2, addr in series:
    print delta1, size, delta2, hex(addr)

  return

if __name__ == '__main__':
  parser = optparse.OptionParser()
  parser.add_option('-f', '--filename', dest='filename', help='snapshot file')
  
  (options, args) = parser.parse_args()
  if not options.filename:
    parser.error('No sample file')

  lastCycle, head, overflow, deltaTable, valueTable = read_snapshot(options.filename)

  parse_data(lastCycle, head, overflow, deltaTable, valueTable)
