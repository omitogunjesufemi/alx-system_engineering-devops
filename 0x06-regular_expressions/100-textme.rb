#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:(?<from>\+?\w+)\])\s(\[to:(?<to>\+?\w+)\])\s(\[flags:(?<flags>-?\d:-?\d:-?\d:-?\d:-?\d)\])/).join(",")
