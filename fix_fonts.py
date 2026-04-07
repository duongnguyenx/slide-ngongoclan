import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(old, new):
    global content
    content = content.replace(old, new)

# Slide 7
replacer('text-lg text-teal-900', 'text-2xl text-teal-900')
replacer('p-4 flex items-center gap-4', 'p-6 flex items-center gap-6')
replacer('text-xl italic leading-relaxed', 'text-2xl italic leading-relaxed')

# Slide 5
replacer('text-sm opacity-80', 'text-xl opacity-80 pt-2')
replacer('text-lg font-medium relative', 'text-2xl font-medium relative')
replacer('text-xl opacity-90 italic', 'text-2xl opacity-90 italic')

# Slide 8
replacer('text-lg opacity-90 leading-snug', 'text-2xl opacity-90 leading-relaxed')
replacer('text-2xl font-bold text-yellow-300', 'text-3xl font-bold text-yellow-300')
replacer('opacity-70 mt-2', 'opacity-80 mt-2 text-lg')
replacer('font-bold text-xl uppercase', 'font-black text-2xl uppercase')
replacer('text-lg flex items-center', 'text-2xl flex items-center')

# Slide 9
replacer('opacity-90 text-blue-800 font-medium text-lg', 'opacity-90 text-blue-800 font-medium text-2xl')

# Slide 11
replacer('text-sm opacity-80 mt-2 text-teal-800', 'text-xl opacity-80 mt-3 text-teal-800')
replacer('font-black text-xl text-teal-900', 'font-black text-2xl text-teal-900')
replacer('font-medium text-lg relative', 'font-medium text-2xl relative space-y-6')
replacer('p-8 rounded-2xl', 'p-12 rounded-2xl')

# Slide 12
replacer('text-red-500 font-bold opacity-80', 'text-red-500 font-bold opacity-80 text-xl')
replacer('text-blue-900 font-black', 'text-blue-900 font-black text-2xl')
replacer('p-4 shadow-sm bg-white', 'p-6 shadow-md bg-white')
replacer('text-sm\">\n                Hormone', 'text-xl\">\n                Hormone')
replacer('<small>pH 5.5</small>', '<span class=\"text-lg opacity-70\">pH 5.5</span>')
replacer('<small>Xà phòng</small>', '<span class=\"text-lg opacity-70\">Xà phòng</span>')

# Slide 13
replacer('font-medium opacity-90 text-lg', 'font-medium opacity-90 text-xl leading-relaxed mt-2')
replacer('font-black text-2xl text-teal-700', 'font-black text-3xl text-teal-700')
replacer('font-black text-2xl text-red-600', 'font-black text-3xl text-red-600')
replacer('font-black text-2xl text-blue-600', 'font-black text-3xl text-blue-600')
replacer('font-black text-2xl text-green-600', 'font-black text-3xl text-green-600')
replacer('text-lg relative z-10 opacity-90', 'text-2xl relative z-10 opacity-90')

# Slide 16
replacer('opacity-90 relative z-10 text-lg', 'opacity-90 relative z-10 text-2xl')
replacer('opacity-100 relative z-10 text-lg', 'opacity-100 relative z-10 text-2xl')
replacer('text-red-500 text-xl', 'text-red-500 text-3xl')
replacer('space-y-4 font-medium', 'space-y-8 font-medium leading-relaxed')
replacer('space-y-6 font-medium', 'space-y-10 font-medium leading-relaxed')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
