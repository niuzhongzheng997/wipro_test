import pandas as pd

def merge_one_to_many(file_a, file_b, merge_column='aws instance'):
    """
    合并一对多关系的CSV文件
    a文件: 一个aws instance对应多行（其他列值不同）
    b文件: 每个aws instance只出现一次
    """
    # 读取CSV文件
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)
    
    # 验证b文件确实没有重复值
    duplicate_count = df_b[merge_column].duplicated().sum()
    if duplicate_count > 0:
        print(f"警告：b文件中发现 {duplicate_count} 个重复的 '{merge_column}' 值")
        print("这与预期不符，请检查数据")
        return None
    
    # 执行left join合并
    merged_df = pd.merge(df_a, df_b, on=merge_column, how='left')
    
    print(f"合并完成！")
    print(f"a文件行数: {len(df_a)}")
    print(f"b文件行数: {len(df_b)}") 
    print(f"合并后行数: {len(merged_df)}")
    
    return merged_df

# 使用示例
if __name__ == "__main__":
    result = merge_one_to_many('a.csv', 'b.csv', 'aws instance')
    
    if result is not None:
        # 保存结果
        result.to_csv('merged_result.csv', index=False)
        print("结果已保存到 merged_result.csv")