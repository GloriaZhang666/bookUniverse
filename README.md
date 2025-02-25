下面是对 commit **8ec2b1c**（Jaal原版，截止2021.10）与 commit **5768e35**（当前）之间差异的详细分析，以及新增功能逻辑的简要说明：

1. **CSV 上传功能**  
   - **新增接口与解析逻辑：** 在当前版本中，增加了一个 CSV 文件上传接口，允许用户通过上传 CSV 文件批量导入图书数据。上传后的 CSV 文件会经过解析，提取图书的各项信息，替代了原本固定数据源的方式。

2. **从 CSV 中提取自定义主题**  
   - **主题抽取与处理：** 在 CSV 文件解析的过程中，新增加了对主题字段的检测和抽取。系统会从 CSV 中提取出所有自定义的主题，并将其整理为一个主题列表，供后续在 UI 中显示。

3. **UI 界面主题选择扩展**  
   - **展示与过滤：** 根据从 CSV 中抽取出的主题，UI 上增加了一个主题选择组件。用户可以根据自己上传数据中定义的主题，选择任意组合进行过滤，达到个性化数据展示的效果。

4. **图书连接逻辑的改进**  
   - **日期顺序建立边：** 无论用户在主题选择中采用何种组合，图书之间的连接（即边）的建立逻辑保持不变，均是依据图书的日期先后顺序来确定。这种逻辑确保了连接关系的统一性和数据展示的连贯性。

总体来说，本次改动主要聚焦在数据导入和个性化展示上：  
- 通过 CSV 上传实现灵活的数据源输入；  
- 利用 CSV 中的主题信息，为用户提供了更多自定义展示的选项；  
- 同时保持了图书之间连接逻辑的简单一致性，即按日期顺序建立连接，确保数据关系的清晰和稳定。

这些改进使得 `bookUniverse` 更贴合用户个性化需求，同时也为后续功能扩展提供了更好的数据支撑。

---
Based on the comparison between commit **8ec2b1c** (base: Jaal until Dec, 2021) and commit **5768e35** (current), here’s an English summary of the changes and the new functionality logic:

1. **CSV Upload Functionality**  
   - **New Interface and Parsing Logic:** A CSV file upload feature has been introduced, allowing users to import book data in bulk. Once uploaded, the CSV file is parsed to extract the necessary book details, replacing the previously fixed data source.

2. **Extraction of Custom Themes from CSV**  
   - **Theme Extraction:** During the CSV parsing process, additional logic extracts the theme fields from the data. The extracted themes are compiled into a list, which is then presented in the UI as filter options.

3. **UI Enhancement for Theme Selection**  
   - **Custom Theme Filtering:** With the newly extracted themes, a theme selection component has been added to the UI. This allows users to filter the displayed books based on their chosen themes, enabling a more personalized and flexible visualization.

4. **Edge (Connection) Logic Based on Dates**  
   - **Consistent Connection Rules:** Regardless of the theme combinations selected, the logic for creating connections (edges) between books remains unchanged. The edges are established based on the chronological order of the books' dates, ensuring a consistent and coherent relationship structure.

Overall, these updates allow users not only to upload their own book data via CSV but also to define and select custom themes for personalized visualization. At the same time, the project maintains a simple, date-based connection logic between books, preserving the clarity of the underlying data relationships.
