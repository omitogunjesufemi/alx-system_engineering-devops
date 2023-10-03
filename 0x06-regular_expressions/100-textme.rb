#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:(?<from>.+)\]\s\[to:(?<to>.+)\]\s\[flags:(?<flags>.+)\]\s\[m)/).join(",")
