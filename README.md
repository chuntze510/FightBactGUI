# FightBactGUI
## 團隊:
FightBact小隊
## 簡介:
Fight Bact的QT GUI 介面撰寫
## 預計功能
- 畫面介紹:
    - 移動按鈕
    - 指令框框
    - 影像顯示
    - 亮度調整
    - 圖片儲存
- 影像處理:
    - 自動對焦
    - 雜訊去除
    - 影像增強
    - 影像翻轉
## 維護人員:
均澤

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

void find_and_extract_xy(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Failed to open file");
        return;
    }

    char line[MAX_LINE_LENGTH];
    int line_number = 1;

    while (fgets(line, sizeof(line), file)) {
        // Remove newline character at the end of the line if it exists
        line[strcspn(line, "\n")] = 0;

        // Check if the line starts with 'X' or 'Y'
        if (line[0] == 'X' || line[0] == 'Y') {
            printf("Line %d starts with '%c': %s\n", line_number, line[0], line);
        }

        line_number++;
    }

    fclose(file);
}

int main() {
    const char *filename = "input.txt"; // Replace with your .txt file name

    printf("Reading file: %s\n", filename);
    find_and_extract_xy(filename);

    return 0;
}

