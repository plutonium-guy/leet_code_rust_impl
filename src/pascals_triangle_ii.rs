struct Solution;
impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let mut result:Vec<i32> = vec![1];
        for i in 0..=row_index as usize{
            result.push(1);
            for j in (1..i).rev(){
                result[j] += result[j-1];
            }

        }
        result
        
    }
}