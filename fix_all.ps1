 = [System.IO.File]::ReadAllText("$pwd/index.html", [System.Text.Encoding]::UTF8)

# 1. Regex to strip <br /> from medium-text exactly safely
 = [System.Text.RegularExpressions.Regex]::Replace(, '(?s)(<h2 class="medium-text[^>]*>\s*)(.*?)(?:<br\s*/?>)\s*(<span class="text-yellow-400">.*?</span>\s*</h2>)', '$1$2 $3')

# 2. Add nowrap explicitly to style (in case my previous attempt failed)
$content = $content.Replace('font-size: 4.5rem;', "font-size: 3.2rem;
        white-space: nowrap;")

# 3. Slide 11
$content = $content.Replace('w-1/2 pl-12 flex flex-col justify-center', 'w-[55%] pl-8 flex flex-col justify-center scale-110 origin-right transition-transform')
$content = $content.Replace('w-1/2 flex justify-center items-center relative', 'w-[45%] flex justify-center items-center relative pl-4')
$content = $content.Replace('bg-teal-800 p-8 rounded-2xl', 'bg-teal-800 p-12 rounded-2xl w-[110%] ml-auto max-w-2xl')

# 4. Slide 12
$content = $content.Replace('w-[45%] flex flex-col justify-center items-center', 'w-[45%] flex flex-col justify-center items-center scale-110 origin-right transition-transform pl-12')
$content = $content.Replace('text-center relative max-w-sm', 'text-center relative max-w-xl w-[120%]')

# 5. Slide 13
$content = $content.Replace('w-1/2 flex justify-center items-center', 'w-[55%] flex justify-center items-center scale-110 origin-right transition-transform pl-12')
$content = $content.Replace('w-1/2 pr-10', 'w-[45%] pr-10')
$content = $content.Replace('absolute right-4 top-1/2 transform -translate-y-1/2 w-16 h-16 text-red-100', 'absolute -right-4 -bottom-4 w-32 h-32 text-red-100 opacity-20 pointer-events-none transform rotate-12')

# 6. Slide 14
$content = $content.Replace('w-7/12 pl-16 flex flex-col justify-center', 'w-[60%] pl-10 flex flex-col justify-center scale-110 origin-right transition-transform')
$content = $content.Replace('w-5/12 flex flex-col justify-center gap-6', 'w-[40%] flex flex-col justify-center gap-6 pr-6')

# 7. Slide 16
$content = $content.Replace('w-1/2 pl-10 flex flex-col justify-center', 'w-[60%] pl-16 flex flex-col justify-center scale-110 origin-right transition-transform')
$content = $content.Replace('w-1/2 pr-10', 'w-[40%] pr-6')

[System.IO.File]::WriteAllText("$pwd/index.html", $content, [System.Text.Encoding]::UTF8)
