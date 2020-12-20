char * toLowerCase(char * str){
    int n = strlen(str);
    for (int i = 0; i < n; i++)
    {
        if ((*(str + i) >= 65) && (*(str + i) <= 90))
        {
            *(str + i) ^= (1 << 5);
        }
    }
    return str;
}
/* A~Z = 65~90
   a~z = 97~122
   大小写字母差值是32.
   异或即加上32，大写转小写。
 */
