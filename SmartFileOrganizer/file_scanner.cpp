#include <iostream>
#include <filesystem>
#include <fstream>

namespace fs = std::filesystem;

int main() {
    std::string folderPath = getenv("HOME") + std::string("/Downloads"); // Change path if needed

    std::ofstream outputFile("output.csv");
    outputFile << "Filename,Extension,Size(Bytes),Path\n";

    for (const auto &file : fs::directory_iterator(folderPath)) {
        if (fs::is_regular_file(file)) {
            std::string filename = file.path().filename().string();
            std::string extension = file.path().extension().string();
            uintmax_t size = fs::file_size(file);
            std::string fullPath = file.path().string();

            outputFile << filename << "," << extension << "," << size << "," << fullPath << "\n";
        }
    }

    outputFile.close();
    std::cout << "✅ File scan complete! Data saved in output.csv\n";
    return 0;
}
