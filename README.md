**项目描述：**

`bookUniverse` 是一个基于 Python 的交互式图书可视化工具，旨在帮助用户以网络图的形式探索和分析图书之间的关系。该项目基于 [Jaal](https://github.com/imohitmayank/jaal/) 库进行开发，Jaal 是一个使用 Dash 和 Visdcc 构建的交互式网络可视化工具。在此基础上，`bookUniverse` 进行了多项定制化修改，以满足特定的图书数据可视化需求。

**主要个性化修改：**

下面是对 commit **8ec2b1c**（Jaal原版，截止2021.10）与 commit **5768e35**（2021.12）之间差异的详细分析，以及新增功能逻辑的简要说明：

1. **CSV 上传功能**  
   - **新增接口与解析逻辑：** 在当前版本中，增加了一个 CSV 文件上传接口，允许用户通过上传 CSV 文件批量导入图书数据。上传后的 CSV 文件会经过解析，提取图书的各项信息，替代了原本固定数据源的方式。
![bookUniverse_csv - 副本](https://github.com/user-attachments/assets/fdc7b76a-54ef-4118-9688-b8210382655d)

2. **从 CSV 中提取自定义主题**  
   - **主题抽取与处理：** 在 CSV 文件解析的过程中，新增加了对主题字段的检测和抽取。系统会从 CSV 中提取出所有自定义的主题，并将其整理为一个主题列表，供后续在 UI 中显示。

3. **UI 界面主题选择扩展**  
   - **展示与过滤：** 根据从 CSV 中抽取出的主题，UI 上增加了一个主题选择组件。用户可以根据自己上传数据中定义的主题，选择任意组合进行过滤，达到个性化数据展示的效果。
![bookUniverse_UI - 副本](https://github.com/user-attachments/assets/3d11efa9-b5a9-476e-a546-be0f8e1f3eed)

4. **图书连接逻辑的改进**  
   - **日期顺序建立边：** 无论用户在主题选择中采用何种组合，图书之间的连接（即边）的建立逻辑保持不变，均是依据图书的日期先后顺序来确定。这种逻辑确保了连接关系的统一性和数据展示的连贯性。

总体来说，本次改动主要聚焦在数据导入和个性化展示上：  
- 通过 CSV 上传实现灵活的数据源输入；  
- 利用 CSV 中的主题信息，为用户提供了更多自定义展示的选项；  
- 同时保持了图书之间连接逻辑的简单一致性，即按日期顺序建立连接，确保数据关系的清晰和稳定。

这些改进使得 `bookUniverse` 更贴合用户个性化需求，同时也为后续功能扩展提供了更好的数据支撑。

---
**Project description:**

bookUniverse is a Python-based interactive book visualization tool designed to help users explore and analyze relationships between books in the form of network diagrams. The project is developed based on the [Jaal](https://github.com/imohitmayank/jaal/) library, an interactive network visualization tool built using Dash and Visdcc. On this basis, bookUniverse has made a number of customized modifications to meet specific book data visualization needs.

**Main personalization modifications:**

Based on the comparison between commit **8ec2b1c** (base: Jaal until Oct, 2021) and commit **5768e35** (Dec, 2021), here’s an English summary of the changes and the new functionality logic:

1. **CSV Upload Functionality**  
   - **New Interface and Parsing Logic:** A CSV file upload feature has been introduced, allowing users to import book data in bulk. Once uploaded, the CSV file is parsed to extract the necessary book details, replacing the previously fixed data source.
![bookUniverse_csv - copy](https://github.com/user-attachments/assets/a9a1c73e-385f-4f63-9db7-c282033f26a6)

2. **Extraction of Custom Themes from CSV**  
   - **Theme Extraction:** During the CSV parsing process, additional logic extracts the theme fields from the data. The extracted themes are compiled into a list, which is then presented in the UI as filter options.

3. **UI Enhancement for Theme Selection**  
   - **Custom Theme Filtering:** With the newly extracted themes, a theme selection component has been added to the UI. This allows users to filter the displayed books based on their chosen themes, enabling a more personalized and flexible visualization.
![bookUniverse_UI - copy](https://github.com/user-attachments/assets/fdae63c6-d247-49b0-b65b-3b8a0f177dc8)

4. **Edge (Connection) Logic Based on Dates**  
   - **Consistent Connection Rules:** Regardless of the theme combinations selected, the logic for creating connections (edges) between books remains unchanged. The edges are established based on the chronological order of the books' dates, ensuring a consistent and coherent relationship structure.

Overall, these updates allow users not only to upload their own book data via CSV but also to define and select custom themes for personalized visualization. At the same time, the project maintains a simple, date-based connection logic between books, preserving the clarity of the underlying data relationships.
